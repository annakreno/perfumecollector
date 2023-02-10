from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('perfumes/', views.perfumes_index, name='index'),
    path('about/', views.about, name='about'),
    path('perfumes/<int:perfume_id>/', views.perfumes_detail, name='detail'),
    path('perfumes/create/', views.PerfumeCreate.as_view(), name='perfumes_create'),
    path('perfumes/<int:pk>/update/', views.PerfumeUpdate.as_view(), name='perfumes_update'),
    path('perfumes/<int:pk>/delete/', views.PerfumeDelete.as_view(), name='perfumes_delete'),
]