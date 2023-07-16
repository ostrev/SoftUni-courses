from django.urls import path

from auth_demos.web.views import AuthView, index, login_user, logout_user
from django.views import generic as views

urlpatterns = [
    path('index-two/', AuthView.as_view(), name='index two'),
    path('index/', index, name='index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', views.TemplateView.as_view(template_name='index.html'), name='auth view' ),
]