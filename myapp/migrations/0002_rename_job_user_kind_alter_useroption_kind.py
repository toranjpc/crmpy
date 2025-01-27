# Generated by Django 5.1.5 on 2025-01-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='job',
            new_name='kind',
        ),
        migrations.AlterField(
            model_name='useroption',
            name='kind',
            field=models.CharField(blank=True, choices=[('UserExtData', 'UserExtData'), ('UserKind', 'UserKind')], max_length=255, null=True),
        ),
    ]
