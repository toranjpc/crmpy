from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils import timezone

class User(AbstractUser):
    
    SEX_CHOICES = [
    (1, 'Male'),
    (2, 'Female'),
    ]


    f_id = models.IntegerField(default=0)
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=1)
    ircode = models.CharField(max_length=20, default="0", blank=True, null=True)
    # name = models.CharField(max_length=100, blank=True, null=True)
    # lastname = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateTimeField(blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)  
    mobile_verified_at = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=191, unique=True, blank=True, null=True)  
    email_verified_at = models.DateTimeField(blank=True, null=True)
    job = models.IntegerField(default=0)
    per = models.JSONField(blank=True, null=True)
    des = models.JSONField(blank=True, null=True)
    # status = models.SmallIntegerField(default=1)
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    # فیلدهای زمان‌بندی
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username