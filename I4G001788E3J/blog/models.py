from django.contrib.auth import get_user_model
from typing import Text
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField(max_length=10000000)
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField()

