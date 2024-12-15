# https://docs.djangoproject.com/en/4.2/topics/http/views/
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader  # Импорт загрузчика шаблонов
from django.shortcuts import render, get_object_or_404

from .models import IPAddressModel

# def index(request):
#     template = 'index.html'
#     return render(request, template) 

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    ips = IPAddressModel.objects.all()[:40]
    # В словаре context отправляем информацию в шаблон
    context = {
        'ips': ips,
    }
    return render(request, 'index.html', context) 

def ips_list(request):
    ips = IPAddressModel.objects.all()[:40]
    context = {
        'ips': ips,
    }
    return render(request, 'ips/ips_list.html', context)
    # return HttpResponse('Список ips')

def ips_detail(request, ip):
    ip = get_object_or_404(IPAddressModel, ip_address=ip)
    context = {
        'ip': ip,
        'posts': 'posts',
    }
    # return HttpResponse(f'Вы указали IP: {ip}') 
    return render(request, 'ips/ips_detail.html', context) 