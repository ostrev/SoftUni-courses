from django.urls import path, include
from expenses_tracker.tracker import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete expense'),

    path('profile/', include([
        path('', views.profile, name='profile'),
        path('create/', views.create_profile, name='create profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ])),

]
