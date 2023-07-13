from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register user'),
    path('login/', views.LoginUserView.as_view(), name='login user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit '),
        path('delete/', views.profile_delete, name='profile delete')

    ])),


]
