from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)