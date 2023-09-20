from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    
    # Вход/регистрация
    path('register/', views.Register.as_view(), name='register'),
    
    # Личный кабинет
    path('', views.personal_account, name='personal_account'),
    path('edit/', views.personal_account_edit, 
         name='personal_account_edit'),
    
    # Тестовые страницы
    path('test/', views.test, name='test'),
]