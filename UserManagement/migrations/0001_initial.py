# Generated by Django 2.2.11 on 2020-11-23 09:14

import UserManagement.common
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_auto_20201123_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroupRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'db_table': 't_user_group_ref',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(20)], verbose_name='用户名')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(20)], verbose_name='昵称')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[UserManagement.common.PhoneValidator()], verbose_name='手机号')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('wx_open_id', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='微信id')),
                ('groups', models.ManyToManyField(blank=True, help_text='用户组', related_name='user_set', related_query_name='user', through='UserManagement.UserGroupRef', to='auth.Group', verbose_name='用户组')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 't_user',
                'permissions': [],
            },
        ),
        migrations.AddField(
            model_name='usergroupref',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
