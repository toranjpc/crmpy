from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from .user_model import User

class App(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, default='عنوان نرم افزار', blank=True)
    sett = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    STATUS_CHOICES = [
        (1, 'Active'),
        (0, 'Inactive'),
    ]
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=1)


    class Meta:
        db_table = 'np_apps'  # استفاده از snake_case برای نام جدول

    def __str__(self):
        return self.title or self.url