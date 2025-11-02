from django.db import models

# Create your models here.

class IsroAchievemnt(models.Model):
    # For Isro history timeline
    year = models.IntegerField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='achievements/', null=True, blank=True)

    # metadata
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return f"{self.year} - {self.title}"
    

class SiteSettings(models.Model):
    # For managing site-wide settings
    site_name = models.CharField(max_length=100, default="ISRO VIMARSH")
    tagline = models.CharField(max_length=200, blank=True)
    about_text = models.TextField(blank=True)
    github_link = models.URLField(blank=True)
    twitter_handle = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name