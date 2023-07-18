from django.urls import path


from user_and_password_demos.web.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]
