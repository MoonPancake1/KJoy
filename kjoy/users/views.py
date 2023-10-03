from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from .forms import *


def test(request):
    """
    Тестовые запросы
    """
    context = {}
    
    return render(request, 'users/test.html', context=context)


def personal_account(request):
    """
    Отображение личного кабинета
    """
    context = {}

    return render(request, 'users/account/personal_account.html', context=context)


@login_required
def personal_account_edit(request):
    """
    Редактирование личного кабинета
    """
    user = request.user.account
    form = EditUserAccountForm(instance=user)

    if request.method == 'POST':
        form = EditUserAccountForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('personal_account')

    context = {
        'form': form,
    }

    return render(request, 'users/account/personal_account_edit.html',
                  context=context)
    

# ====================================================
#  Функции для предоставления информации пользователю
# ====================================================
def main(request):
    """
    Отображение главной страницы
    """
    context = {}

    return render(request, 'users/index.html', context=context)


def password_generate(request):
    """
    Отображение страницы для генерации паролей
    """
    context = {}

    return render(request, 'users/password_generate.html', context=context)


def price(request):
    """
    Отображение страницы с тарифами
    """
    context = {}

    return render(request, 'users/price.html', context=context)


def faqs(request):
    """
    Отображение страницы faq
    """
    context = {}

    return render(request, 'users/faqs.html', context=context)


def about(request):
    """
    Отображение страницы с информацией о нас
    """
    context = {}

    return render(request, 'users/about.html', context=context)


# =========================================
#  Функции связанные с регистрацией/входом
# =========================================
class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            Account.objects.create(user=user)
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('personal_account')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
