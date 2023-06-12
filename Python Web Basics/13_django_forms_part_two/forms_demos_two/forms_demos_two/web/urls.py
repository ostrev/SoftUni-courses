from django.urls import path

from forms_demos_two.web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.list_persons, name='list person'),
    path('persons/create/', views.create_person, name='create person'),

]