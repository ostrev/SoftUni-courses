from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram.common.forms import CommentForm, SearchPhotosForm
from petstagram.common.models import Like
from petstagram.photos.models import Photo


# Create your views here.

def index(request):

    search_form = SearchPhotosForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    all_photos = Photo.objects.all()
    user = request.user
    all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
    if search_pattern:
        all_photos = all_photos.filter(tagged_pets__name__icontains=search_pattern)
    print(all_photos)
    context = {
        'all_photos': all_photos,
        'comment_form': CommentForm(),
        'search_form': search_form,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    # to_photo = photo_id
    # to_photo_id = photo.id
    # to_photo = photo

    kwargs = {
        'to_photo': photo,
        'user': request.user
    }
    like_obj = Like.objects.filter(**kwargs).first()

    if like_obj:
        like_obj.delete()
    else:
        new_like_obj = Like(**kwargs)
        new_like_obj.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


@login_required
def share_functionality(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


@login_required
def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.filter(pk=photo_id).get()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # Does not commit to DB
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
