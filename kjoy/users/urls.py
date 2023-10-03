from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    
    # Вход/регистрация
    path('register/', views.Register.as_view(), name='register'),
    
    # Личный кабинет
    path('account/', views.personal_account, name='personal_account'),
    path('edit/', views.personal_account_edit, 
         name='personal_account_edit'),
    
    # Пользовательские страницы
    path('', views.main, name='main'),
    path('password_generate/', views.password_generate, name='password_generate'),
    path('price/', views.price, name='price'),
    path('FAQs/', views.faqs, name='faqs'),
    path('about/', views.about, name='about'),
    
    # Тестовые страницы
    path('test/', views.test, name='test'),
]