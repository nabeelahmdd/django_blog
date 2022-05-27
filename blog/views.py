from django.shortcuts import render, get_object_or_404
from django.views import generic
from blog.models import (
    Article, Category, Comment
)
from django.db.models import Q
from blog.forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
# Create your views here.

class ArticleList(generic.ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = 6
    queryset = Article.objects.filter(is_active=True)

    def get_queryset(self):
        qs = Article.objects.all().select_related('primary_category')
        category = self.request.GET.get('category', None)
        search = self.request.GET.get('search', None)
        if search:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(primary_category__name__icontains=search)
            ).distinct()
        if category:
            qs = qs.filter(Q(primary_category__name=category) |
                           Q(secondary_categories__name=category)).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context.update({
            "recent_article": Article.objects.all().order_by('-cr_date')[0:4],
            "categories": Category.objects.all(),
            "search": self.request.GET.get('search', None),
        })
        return context


class ArticleDetail(
    SuccessMessageMixin,
    generic.FormView):
    template_name = 'blog/detail.html'
    form_class = CommentForm
    success_message = "Comment Has been Created!"
    def get_object(self):
        return get_object_or_404(Article, slug=self.kwargs["slug"])


    def get_success_url(self, **kwargs):
        return reverse(
            'article-detail', kwargs={'slug': self.get_object().slug}
        )

    def form_valid(self, form):
        forms = form.save(commit=False)
        forms.article = self.get_object()
        forms.save()
        return super(ArticleDetail, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context.update({
            "object": self.get_object(),
            "categories": Category.objects.all(),
            "comment_count": Comment.objects.filter(
                article__slug=self.kwargs["slug"]
            ).count(),
            "comment": Comment.objects.filter(
                article__slug=self.kwargs["slug"]
            ),
            "recent_article": Article.objects.all().order_by('-cr_date')[0:4],
        })
        return context