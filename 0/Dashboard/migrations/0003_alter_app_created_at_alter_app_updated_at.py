# Generated by Django 5.1.5 on 2025-01-18 13:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_alter_app_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
