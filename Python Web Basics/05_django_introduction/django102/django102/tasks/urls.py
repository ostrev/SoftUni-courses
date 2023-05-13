from django.urls import path

from django102.tasks.views import index

urlpatterns = (
    path('', index),
)