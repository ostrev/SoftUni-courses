from django.urls import path

from expenses_tracker.tracker import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete expense'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.profile_create, name='create profile'),
    path('profile/edit/', views.profile_edit, name='edit profile'),
    path('profile/delete/', views.profile_delete, name='delete profile'),

]






