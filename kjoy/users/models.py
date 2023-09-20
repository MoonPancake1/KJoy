import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.deconstruct import deconstructible
from .utils import crop_image


class User(AbstractUser):
    def __str__(self):
        return f"{self.id}. {self.username}"


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    role = models.CharField(
        'Роль пользователя',
        null=True,
        blank=True,
        max_length=50,
        choices=[
            ('Пользователь', 'Пользователь'),
            ('Основатель', 'Основатель'),
        ],
        default='Пользователь'
    )
    img = models.ImageField('Аватар', null=True, blank=True, upload_to=PathAndRename("img/avatar/"),
                            default='img/avatar/standard_avatar.png')

    def save(self, **kwargs):
        """Метод редактирует картинку пользователя"""
        super().save()
        crop_image(self.img.path)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь_доп'
        verbose_name_plural = 'Пользователи_доп'


class PasswordUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField('Адрес сайта', max_length=255)
    login = models.CharField('Логин', max_length=255)
    password = models.CharField('Пароль', max_length=255)
    password_hash = models.CharField('Хэш пароля', max_length=64)
    detail = models.TextField('Детали записи')

    def __str__(self):
        return f'{self.id}. {self.url} : {self.login}'

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'