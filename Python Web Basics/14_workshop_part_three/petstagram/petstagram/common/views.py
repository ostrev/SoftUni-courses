from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.

def index(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    # to_photo = photo_id
    # to_photo_id = photo.id
    # to_photo = photo
    like_obj = Like.objects.filter(to_photo=photo_id).first()

    if like_obj:
        like_obj.delete()
    else:
        new_like_obj = Like(to_photo=photo)
        new_like_obj.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")
