from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from jdatetime import date as jdate
from django.utils import timezone

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
    per = models.JSONField(blank=True, null=True)
    des = models.JSONField(blank=True, null=True)
    # status = models.SmallIntegerField(default=1)
    remember_token = models.CharField(max_length=100, blank=True, null=True)

    # فیلدهای زمان‌بندی
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # kind = models.IntegerField(default=0)
    kind = models.ForeignKey(
        'UserOption',
        related_name='user_category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        limit_choices_to={'kind': 'UserCategory'},
        to_field='id'
    )

    groups = models.ManyToManyField(
        'UserOption',
        related_name='user_groups',
        blank=True,
        limit_choices_to={'kind': 'UserGroup'}
    )

    @property
    def birth_shamsi(self):
        if self.birth:
            # تبدیل به timezone محلی
            local_date = timezone.localtime(self.birth).date()
            return jdate.fromgregorian(date=local_date).strftime('%Y/%m/%d')
        return None

    def __str__(self):
        return self.username
    
class UserOption(models.Model):
    f_id = models.IntegerField(default=0)
    title = models.CharField(max_length=255, null=True, blank=True)
    option = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    KIND_CHOICES = [
        ('UserExtData', _('UserExtData')), 
        ('UserCategory', _('user kinds')), 
        ('UserGroup', _('user Groups')), 
    ]
    kind = models.CharField(choices=KIND_CHOICES, max_length=255, null=True, blank=True)

    Status_CHOICES = [
    (0, _('not active')),
    (1, _('active')),
    ]
    status = models.SmallIntegerField(choices=Status_CHOICES, default=0)

    class Meta:
        db_table = 'myapp_user_options'

    def __str__(self):
        return self.title or f"UserOption {self.id}"
    