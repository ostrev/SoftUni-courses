from django.urls import path
from django_template_demo.template_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments page')
]