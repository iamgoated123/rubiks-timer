from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User1(User):
    pass


class Solve(models.Model):
    time = models.FloatField()
    scramble = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

