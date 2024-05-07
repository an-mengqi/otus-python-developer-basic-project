from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class OtusUser(AbstractUser):
    bio = models.TextField('biography', blank=True)
