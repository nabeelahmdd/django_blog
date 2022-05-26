from django.views import generic
from blog.models import Article, Category
from django.db.models import Q
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