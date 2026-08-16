from django.shortcuts import get_object_or_404, render, redirect
from phones.management.commands.import_phones import Command
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort')
    template = 'catalog.html'
    if sort_param == 'name':
        phones = Phone.objects.all().order_by('slug')
    elif sort_param == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
