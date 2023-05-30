from django import template

register = template.Library()


@register.filter(name='find_long_name')
def find_long_name(students):
    long_students = []
    for student in students:
        if len(student) > 4:
            long_students.append(student)

    return long_students

