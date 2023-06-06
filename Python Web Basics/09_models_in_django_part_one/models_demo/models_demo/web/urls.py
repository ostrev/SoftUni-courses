from django.urls import path
from models_demo.web import views

urlpatterns = [
    path('', views.home_page, name='index')

]