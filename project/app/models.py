from django.db import models

# Create your models here.

class item(models.Model):
    content = models.CharField(max_length=50, null=False)