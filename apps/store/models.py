from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Shirt(models.Model):
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=1)
    fabric = models.CharField(max_length=60)
    fabricator = models.ForeignKey(User, related_name = 'all_shirts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
