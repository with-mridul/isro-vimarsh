from django.db import models

# Create your models here.
class Rocket(models.Model):
    # Basic Info
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    description = models.TextField()

    #Specification
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in meters")
    diameter = models.DecimalField(max_digits=5, decimal_places=2, help_text="Diameter in meters")
    mass = models.IntegerField(help_text="Mass in Kg")
    stages = models.IntegerField(help_text="Number of Stages")
    payload_capacity_leo = models.IntegerField(help_text="Payload to LEO in kg")
    payload_capacity_geo = models.IntegerField(null=True, blank=True, help_text="Payload to GEO in Kg")

    #Launch Information
    first_launch = models.DateField(null=True, blank=True)
    total_launches = models.IntegerField(default=0)
    successful_launches = models.IntegerField(default=0)

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('retired', 'Retired'),
        ('developement', "In Developement")
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    #Media
    image = models.ImageField(upload_to='rockets/', null=True, blank=True)

    def sucess_rate(self):
        if self.total_launches == 0:
            return 0
        return round((self.successful_launches/ self.total_launches) *100, 2)