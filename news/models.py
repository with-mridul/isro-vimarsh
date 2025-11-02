from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    # content
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)

    #categorization
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    
    # source information
    source_url = models.URLField(blank=True, help_text="Original article URL")
    source_name = models.CharField(max_length=100, blank=True)
    
    # media
    featured_image = models.ImageField(upload_to='news/', null=True, blank=True)
    
    # dates
    published_date = models.DateTimeField()
    scraped_date = models.DateTimeField(auto_now_add=True)
    
    # status
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    # metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title