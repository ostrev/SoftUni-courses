from django import template

register = template.Library()


@register.simple_tag
def show_student_name(student):
    # Student.object.get(student.id).courses.length

    return f"Name is: {student}"


@register.inclusion_tag(
    'template_app/tags/car_info.html',
    name='car_inclusion_tag',
)
def inclusion_car_info(car):
    context = {
        'car': car,
    }
    return context
