from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.views import View
from .forms import *


def test(request):
    return HttpResponse("It's pages need for testing request!")


@login_required
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
