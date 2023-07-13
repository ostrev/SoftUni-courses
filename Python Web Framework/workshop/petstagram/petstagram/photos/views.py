from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from petstagram.common.forms import CommentForm
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo

from django.views import generic as views


@login_required
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


class PhotoAddView(views.CreateView):
    template_name = 'photos/photo-add-page.html'
    model = Photo
    form_class = PhotoCreateForm

    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('photo details', kwargs={
            'pk': self.object.pk
        })

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.user = self.request.user
        return form

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


@login_required
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


@login_required
def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')
