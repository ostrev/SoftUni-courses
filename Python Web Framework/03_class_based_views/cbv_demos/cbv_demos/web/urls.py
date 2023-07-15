from django.urls import path

from cbv_demos.web.views import IndexView, list_article, ListArticleView, RedirectToArticle, DetailArticleView, \
    CreateArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', list_article, name='list article'),
    path('cbv/', ListArticleView.as_view(), name='cbv'),
    path('cbv/<int:pk>/', DetailArticleView.as_view(), name='details article'),
    path('cbv/create/', CreateArticleView.as_view(), name='create article'),
    path('cbv/update/<int:pk>', UpdateArticleView.as_view(), name='update article'),
    path('cbv/delete/<int:pk>', DeleteArticleView.as_view(), name='delete article'),
    # path('cbv/<int:pk>/', ListArticleView.as_view(), name='cbv'),
    path('redirect/', RedirectToArticle.as_view(), name='redirect to article'),
]