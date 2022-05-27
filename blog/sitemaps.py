from django.contrib.sitemaps import Sitemap

from blog.models import Article

class ArticleSitemap(Sitemap):
		changefreq = "always"
		
		def items(self):
				return Article.objects.all()
		
		def lastmod(self, obj):
				return obj.up_date


