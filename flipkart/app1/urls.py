from django.core.management import templates
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('test/', views.test_fun),
    path('test2/', views.test_fun2),
    path('test3/', views.test_fun3),


]
