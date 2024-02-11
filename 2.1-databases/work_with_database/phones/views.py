from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_page = request.GET.get('sort')
    if sort_page == 'name':
        context = {
            'phones': Phone.objects.order_by('name').all()
        }
    elif sort_page == 'min_price':
        context = {
            'phones': Phone.objects.order_by('price').all()
        }
    elif sort_page == 'max_price':
        context = {
            'phones': Phone.objects.order_by('-price').all()
        }
    else:
        context = {
            'phones': Phone.objects.order_by('id').all()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug)
    }
    return render(request, template, context)
