# https://docs.djangoproject.com/en/4.2/topics/http/views/
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse
from django.template import loader  # Импорт загрузчика шаблонов
from django.shortcuts import render, get_object_or_404, redirect

from .models import IPAddressModel
from .forms import IPAddressUpdateForm

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
    ips = IPAddressModel.objects.all()
    paginator = Paginator(ips, 500) 
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'ips/ips_list.html', context)

# @login_required
# def ips_detail(request, ip):
#     ip = get_object_or_404(IPAddressModel, ip_address=ip)
#     context = {
#         'ip': ip,
#         'posts': 'posts',
#     }
#     return render(request, 'ips/ips_detail.html', context) 


@login_required
def ips_detail(request, ip):
    # Получаем IP-адрес или возвращаем 404
    ip_instance = get_object_or_404(IPAddressModel, ip_address=ip)

    if request.method == 'POST':
        form = IPAddressUpdateForm(request.POST, instance=ip_instance)
        if form.is_valid():
            # Устанавливаем пользователя, сделавшего изменения
            ip_instance.user = request.user
            form.save()
            return redirect('ips:var_ips_detail', ip=ip)  # Перенаправление на ту же страницу
    else:
        form = IPAddressUpdateForm(instance=ip_instance)

    context = {
        'ip': ip_instance,
        'form': form,
    }
    return render(request, 'ips/ips_detail.html', context)
