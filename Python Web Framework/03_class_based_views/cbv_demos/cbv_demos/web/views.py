from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from cbv_demos.web.models import Article

from django import forms


# class BaseView:
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
#
#     @classmethod
#     def as_view(cls):
#         self = cls()
#
#         def view(request):
#             if request.method == 'GET':
#                 return self.get(request)
#             else:
#                 return self.post(request)
#
#         return view


class IndexView(views.View):
    def get(self, request):
        return render(request, 'index.html')


def list_article(request):
    context = {
        'articles': Article.objects.all(),

    }

    return render(request, 'article/list.html', context)


# views.CreateView
# views.ListView
# views.UpdateView
# views.DetailView
# views.DeleteView

# class ListArticleView(views.View):
#     def get(self, request, *args, **kwargs):
#         print(self.request)
#         print(self.args)
#         print(self.kwargs)
#         context = {
#             'articles': Article.objects.all(),
#
#         }
#
#         return render(request, 'article/list.html', context)

# class ListArticleView(views.TemplateView):
#     template_name = 'article/list.html'
#     # # Static data
#     # extra_context = {
#     #     'articles': Article.objects.all(),
#     # }
#
#     # dynamic data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context

class RedirectToArticle(views.RedirectView):
    url = reverse_lazy('index')


class ListArticleView(views.ListView):
    model = Article
    template_name = 'article/list-list-view.html'

    # context_object_name = 'articles'
    paginate_by = 5

    # Article.objects.filter(name_icontains=search)
    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class DetailArticleView(views.DetailView):
    model = Article
    template_name = 'article/detail.html'


# class ArticleForm(forms.ModelForm):
#     pass

class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        # fields = self.disabled_fields \
        # if self.disabled_fields != '__all__' \
        # else

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


class CreateArticleView(DisabledFormFieldsMixin, views.CreateView):
    model = Article
    template_name = 'article/create.html'
    fields = ('title', 'content')
    # form_class = ArticleForm
    disabled_fields = ('title',)
    success_url = reverse_lazy('cbv')
    # form_class = modelform_factory(
    #     Article, fields=('content',),
    #     widgets={
    #         'content': forms.TextInput(
    #             attrs={
    #                 'class': 'abcd'
    #             }
    #         )
    #     }
    # )


class UpdateArticleView(views.UpdateView):
    model = Article
    template_name = 'article/update_view.html'
    fields = '__all__'
    success_url = reverse_lazy('cbv')


class DeleteArticleView(DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('cbv')

    form_class = modelform_factory(
        Article, fields=('title', 'content',),

    )
    disabled_fields = ('title', 'content')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)

        return form_kwargs
