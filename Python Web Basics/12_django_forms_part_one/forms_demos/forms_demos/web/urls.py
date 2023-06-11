from django.urls import path

from forms_demos.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('model-form/', views.model_form_view, name='model form view'),
    path('model-form-update/<int:pk>/', views.model_form_update, name='model form update'),

]