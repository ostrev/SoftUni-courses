from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


# Create your views here.
def home(request):
    context = {}

    return render(request, 'urls_and_views_app/main.html', context)


def navbar_page(request):
    return render(request, 'urls_and_views_app/navbar.html')


def departments_page(request):
    return render(request, 'urls_and_views_app/departments.html', )


def departments_page_group(request, group_id):
    if group_id == '1':
        group_name = 'One'
    elif group_id == '2':
        group_name = 'Two'
    else:
        group_name = 'No Group'

    context = {'group_name': group_name}

    return render(request, 'urls_and_views_app/departments.html', context)


def redirect_page(request):
    return redirect('home')


def error_page(request):
    raise Http404
