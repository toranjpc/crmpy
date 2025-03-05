# Generated by Django 5.1.5 on 2025-03-04 18:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_id', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('option', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind', models.CharField(blank=True, choices=[('UserExtData', 'UserExtData'), ('UserCategory', 'user kinds'), ('UserGroup', 'user Groups')], max_length=255, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'not active'), (1, 'active')], default=0)),
            ],
            options={
                'db_table': 'myapp_user_options',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('f_id', models.IntegerField(default=0)),
                ('sex', models.SmallIntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1)),
                ('ircode', models.CharField(blank=True, default='0', max_length=20, null=True)),
                ('birth', models.DateTimeField(blank=True, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('mobile_verified_at', models.DateTimeField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=191, null=True, unique=True)),
                ('email_verified_at', models.DateTimeField(blank=True, null=True)),
                ('per', models.JSONField(blank=True, null=True)),
                ('des', models.JSONField(blank=True, null=True)),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('kind', models.ForeignKey(blank=True, default=None, limit_choices_to={'kind': 'UserCategory'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_category', to='myapp.useroption')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(blank=True, default='عنوان نرم افزار', max_length=255)),
                ('sett', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'np_apps',
            },
        ),
    ]
