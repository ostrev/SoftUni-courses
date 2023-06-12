from django.http import HttpResponse
from django.shortcuts import render

from .forms import TodoCreateForm, TodoForm, PersonCreateForm
from .models import Person


# def index(request):
#     if request.method == 'GET':
#         form = TodoCreateForm()
#     else:
#         form = TodoCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # model = form.instance
#             # model.full_clean()
#             return HttpResponse('All is valid')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'web/index.html', context)

def index(request):
    form_class = TodoForm
    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)
        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'web/index.html', context)

    # # This is sample for get data direct to the form
    # form = TodoForm(
    #     data={
    #         'text': 'Wash the dishes',
    #         'is_done': False,
    #     }
    # )
    # if form.is_valid():
    #     return HttpResponse('All is valid')
    # return HttpResponse('Invalid form')


def list_persons(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'web/list-person.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'web/create-person.html', context)