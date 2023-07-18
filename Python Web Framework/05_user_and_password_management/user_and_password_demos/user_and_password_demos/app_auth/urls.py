from django.urls import path

from user_and_password_demos.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, UserListView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('list_view/', UserListView.as_view(), name='list view'),
]
