
from django.urls import path
from blog.views import  *


urlpatterns = [
    path('', ArticleList.as_view(), name='blog-list'),
    path('blog/<str:slug>/', ArticleDetail.as_view(), name='article-detail'),
]