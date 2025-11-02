from django.db import models

class Mission(models.Model):
    # basic information
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    objectives = models.TextField(help_text="Mission objectives")
    
    # mission type
    MISSION_TYPE_CHOICES = [
        ('lunar', 'Lunar Mission'),
        ('mars', 'Mars Mission'),
        ('solar', 'Solar Mission'),
        ('earth', 'Earth Observation'),
        ('navigation', 'Navigation'),
        ('communication', 'Communication'),
        ('human', 'Human Spaceflight'),
        ('other', 'Other'),
    ]
    mission_type = models.CharField(max_length=20, choices=MISSION_TYPE_CHOICES)
    
    # status
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('development', 'In Development'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    
    # dates
    launch_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
    # associated rocket
    rocket_used = models.CharField(max_length=100, blank=True)
    
    # achievements
    key_achievements = models.TextField(blank=True)
    
    # media
    mission_image = models.ImageField(upload_to='missions/', null=True, blank=True)
    mission_patch = models.ImageField(upload_to='missions/patches/', null=True, blank=True)
    
    # display on homepage
    featured_on_homepage = models.BooleanField(default=False)
    homepage_order = models.IntegerField(default=0, help_text="Order in slideshow")
    
    # metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-launch_date']
    
    def __str__(self):
        return self.name