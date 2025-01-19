from django.db import models
from django.utils import timezone

class App(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    sett = models.JSONField(null=True, blank=True) 
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)  # این خط
    updated_at = models.DateTimeField(default=timezone.now, null=True, blank=True)  # این خط

    class Meta:
        db_table = 'apps'

    def __str__(self):
        return self.title or self.url