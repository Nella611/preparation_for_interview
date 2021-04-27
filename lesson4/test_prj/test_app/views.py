from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from rest_framework import serializers

from .forms import AddForm
from .models import GoodItem



def index(request):
    goods = GoodItem.objects.all()
    if request.method == 'POST':
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddForm()
    contex = {
        'goods': goods,
        'form': form
    }
    return render(request, 'index.html', context=contex)




def catalog(request):
    all_goods = GoodItem.objects.all()
    context = {
        'page_header': 'Каталог товаров',
        'goods': all_goods,
    }
    return render(request, template_name='catalog.html', context=context)


def add_good(request):
    if request.method == 'POST':
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddForm()
    contex = {'form': form}
    return render(request, 'add_good.html', contex)


def ajax_handler(request):
    goods = GoodItem.objects.all()
    data = serializers.serialise('json', goods)
    return HttpResponse(data, content_type='text/html')


