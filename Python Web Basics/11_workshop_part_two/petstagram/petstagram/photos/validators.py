from django.core.exceptions import ValidationError


def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum file size that cen be uploaded is 5MB')
