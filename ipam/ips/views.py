# https://docs.djangoproject.com/en/4.2/topics/http/views/
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader  # Импорт загрузчика шаблонов
from django.shortcuts import render

def index(request):
    template = 'index.html'
    return render(request, template) 

def ips_list(request):
    return HttpResponse('Список ips')

def ips_detail(request, pk):
    return HttpResponse(f'Вы указали IP: {pk}') 