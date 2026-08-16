from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    slug = models.SlugField(auto_created=True,)
    image = models.URLField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    release_date = models.CharField()
    lte_exists = models.BooleanField()

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        ...
