from django.urls import path
from models_demo.web import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('delete/<int:pk>/', views.delete_employee, name='delete employee'),
    path('department/<int:pk>/<slug:slug>/', views.department_details, name='department details'),
]