from django.db import models

# Create your models here.
class Event(models.Model):
    Status = (
        ('Secure','Secure'),
        ('Unsecure','Unsecure'),
    )
    imageName = models.CharField(max_length=200,null=True)
    messege = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=10, null=True, choices=Status)