from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User1(User):
    pass


class Solve(models.Model):
    time = models.CharField(max_length=150)
    scramble = models.CharField(max_length=150)

