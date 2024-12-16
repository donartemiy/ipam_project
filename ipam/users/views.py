"""Что тут происходит?
В шаблон users/signup.html будет отправлена форма с полями,
описанными в классе CreationForm. После заполнения этой формы
пользователь будет переадресован на страницу, для которой в urls.py
указано имя name='posts:index'. Данные, отправленные через форму,
будут переданы в модель User и сохранены в БД.
"""

from django.views.generic import CreateView
# Функция reverse_lazy позволяет получить URL по параметрам функции path()
from django.urls import reverse_lazy
# Импортируем класс формы, что бы сослаться на неё во view-классе
from .forms import CreationForm
from django.shortcuts import render, get_object_or_404
from ips.models import IPAddressModel

from django.contrib.auth import get_user_model
User = get_user_model() 


class SignUp(CreateView):
    # Создаем объект формы
    form_class = CreationForm
    # success_url - URL-адрес для перенаправления
    # после успешной обработки формы.
    # Почему именно reverse_lazy ?
    success_url = reverse_lazy('ips:var_ips')

    # template_name — имя шаблона, куда будет передана переменная form
    template_name = 'users/signup.html'

# Отсальные пути обрабатываются стандартным обработчиком,
# см. users/urls.py


def profile(request, username):
    if request.user.username == username:
        user_instance = get_object_or_404(User, username=username)
        ips_user = user_instance.ip_user.all()
        context = {
            'ips_user': ips_user,
            'user_instance': user_instance
        }
        return render(request, 'users/profile.html', context)
    else:
        return render(request, 'users/login.html', context)