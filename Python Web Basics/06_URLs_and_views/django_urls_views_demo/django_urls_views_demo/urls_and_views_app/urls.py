from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('navbar/', views.navbar_page, name='navbar'),
    path('departments/', views.departments_page, name='departments'),
    path('departments/<str:group_id>', views.departments_page_group, name='departments group'),
    path('test_redirect', views.redirect_page, name='redirect page')
]