from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(
    	null=True, upload_to='article_images'
    )
    body = HTMLField()
    primary_category = models.ForeignKey(
        Category, related_name='primary_products',
        on_delete=models.CASCADE
    )
    secondary_categories = models.ManyToManyField(
    	Category, blank=True
    )

    meta_name = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.CharField(
    	max_length=250, null=True, blank=True
    )

    is_active = models.BooleanField(default=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['cr_date']
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
    	Article,on_delete=models.CASCADE,
        related_name='comments', null=True, blank=True
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    is_active = models.BooleanField(default=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['cr_date']
        verbose_name_plural = "Comments"

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Like(models.Model):
    article = models.ForeignKey(
    	Article, on_delete=models.CASCADE,
        related_name='likes'
    )
    
    cr_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now_add=True)