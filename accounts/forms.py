from operator import mod
from pyexpat import model
from django import forms
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect




class UserCreatForm(UserCreationForm):
    
    class Meta:
        fields = ('first_name', 'last_name', 'username','email','password1','password2')
        model = get_user_model()
        
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['first_name'].lebel= 'First Name'
            self.fields['last_name'].lebel = 'Last Name'
            self.fields['username'].lebel = 'Display Name'
            self.fields['email'].lebel = 'Email Address'
            