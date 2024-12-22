# https://docs.djangoproject.com/en/4.2/topics/http/views/
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView

# Create your views here.
from django.http import HttpResponse
from django.template import loader  # Импорт загрузчика шаблонов
from django.shortcuts import render, get_object_or_404, redirect

from .models import IPAddressModel
from .forms import IPAddressUpdateForm


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


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['just_title'] = 'Info'
        context['just_text'] = ('Это IPAM (IP Address Management) система. В тестовой сети у нас отсутствует DHCP, т.к. в нашей области деятельности нужна высокая надёжность и нельзя полагаться на широковещательную рассылку. Перед/при подключении нового устройства к тестовой сети нам необходимо для него выбрать свободный ip адрес. Данный сервис содержит пользователей, список ip адресов. Пользователи могут резервировать IP адреса и оставлять комментарии. Дополнительно добавлен сервис, который проверяет какие IP адреса сейчас "онлайн" в тестовой сети. Проверка выполняется командой arping -c 2 -w 3')
        return context 