from django.http import HttpResponse
from django.shortcuts import render
from .models import GoodItem


def index(request):
    return HttpResponse(f'hello, {request.user.username}')


def catalog(request):
    all_goods = GoodItem.objects.all()
    context = {
        'page_header': 'Каталог товаров',
        'goods': all_goods,
    }
    return render(request, template_name='catalog.html', context=context)




