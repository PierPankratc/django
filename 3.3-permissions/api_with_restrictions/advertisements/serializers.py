from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        
        request = self.context.get('request')
        user = request.user

        if self.instance is not None:
            new_status = data.get('status')
            if new_status and new_status != self.instance.status:
                allowed_transitions = {
                    'draft': ['open', 'closed'],
                    'open': ['closed'],
                    'closed': [],
                }
                if new_status not in allowed_transitions.get(self.instance.status, []):
                    raise serializers.ValidationError(
                        f"Нельзя изменить статус с '{self.instance.status}' на '{new_status}'."
                    )

        new_status = data.get('status')
        
        if self.instance is None:
            will_be_open = new_status == 'open'
        else:
            will_be_open = (new_status or self.instance.status) == 'open'

        if will_be_open:
            open_count = Advertisement.objects.filter(
                creator=user,
                status='open'
            ).count()

            if self.instance is not None and self.instance.status == 'open':
                open_count -= 1

            if open_count >= 10:
                raise serializers.ValidationError(
                    f"У вас уже 10 открытых объявлений. "
                    f"Закройте одно из них, чтобы открыть новое."
                )

        return data

        
