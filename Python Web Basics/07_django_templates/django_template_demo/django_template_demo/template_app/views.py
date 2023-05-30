from django.shortcuts import render


# Create your views here.

class Car:
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour

    def get_colour(self):
        return self.colour


sport_car = Car("TOYOTA", 'LAND CRUISER', 'Black')


def index(request):
    students = ['Petar', 'Nikolay', 'Anna', 'Pavel', 'Maria']
    context = {'students': students,
               "car_obj": [
                   Car('BMW', "116", 'red'),
                   Car('Audi', "a4", 'blue'),
                   Car("TOYOTA", 'LAND CRUISER', 'Black')
               ],
               }

    return render(request, 'template_app/home_page.html', context)


def departments(request):
    context = {}
    return render(request, 'template_app/departments_page.html', context)
