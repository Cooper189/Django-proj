from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.index, name='index'),
    path('set/', views.setKo, name='setKo')
]
