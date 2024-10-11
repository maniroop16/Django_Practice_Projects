from django.db import models
from django.contrib.auth.models import AbstractUser
from Accounts.manager import *

# Create your models here.
class CustomUser(AbstractUser):

    #username = None
    phone_number = models.CharField(max_length=10, unique=True)
    user_bio = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    user_profile = models.ImageField(upload_to="profile_pictures")

    USERNAME_FIELD = ""
    REQUIRED_FIELDS = []
    objects = UserManager()



