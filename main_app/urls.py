from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfumes/', views.perfumes_index, name='index'),
    path('about/', views.about, name='about'),
    path('perfumes/<int:perfume_id>/', views.perfumes_detail, name='detail'),
    path('perfumes/add', views.add_perfume, name='add_perfume'),
]