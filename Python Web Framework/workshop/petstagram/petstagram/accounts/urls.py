from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register user'),
    path('login/', views.LoginUserView.as_view(), name='login user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile edit '),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile delete')
    ])),
]
