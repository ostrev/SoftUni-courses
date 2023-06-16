from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from petstagram.photos.models import Photo


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        "likes": likes,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'photos/photo-details-page.html', context)


def photo_add(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def photo_edit(request, pk):
    instance = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=instance)
    else:
        form = PhotoEditForm(request.POST, instance=instance)
        if form.is_valid():
            photo = form.save()
            return redirect('photo details', pk=photo.pk)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')

