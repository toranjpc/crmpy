# Generated by Django 5.1.5 on 2025-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_id', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('kind', models.CharField(blank=True, max_length=255, null=True)),
                ('option', models.JSONField(blank=True, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'useroptions',
            },
        ),
    ]
