from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainREST, name='REST'),
]
