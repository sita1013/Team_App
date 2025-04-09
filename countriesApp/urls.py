from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country_list'),
    path('countries/<str:country_code>/', views.country_detail, name='country_detail'),
]
