from django.urls import path
from . import views

app_name = 'tree_menu'

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # О нас
    path('services/', views.services, name='services'),  # Услуги
    path('contacts/', views.contacts, name='contacts'),  # Контакты
    path('services/web-development/', views.web_development, name='web-development'),  # Веб-разработка
    path('services/seo/', views.seo, name='seo'),  # SEO
    path('services/design/', views.design, name='design'),  # Дизайн
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),  # Политика конфиденциальности
]