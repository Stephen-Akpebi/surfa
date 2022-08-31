import email
from django import forms
from os import name
from django.db import models
from operator import mod
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth

# Create your models here.



class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
