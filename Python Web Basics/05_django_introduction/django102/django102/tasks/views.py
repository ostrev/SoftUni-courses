from django.shortcuts import render

# Create your views here.

# from tasks.models import Task

from django import http
def index(request):

    # tasks_list = Task.objects.all()
    # output = "; ".join(f"{t.task_title}: {t.task_text}"
    #                    for t in tasks_list)
    #
    # if not output:
    #     output = "There are no created tasks!"
    return http.HttpResponse('It is works')
