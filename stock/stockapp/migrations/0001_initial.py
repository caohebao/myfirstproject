# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('age', models.IntegerField(null=True, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84', blank=True)),
                ('profession', models.CharField(max_length=128, verbose_name=b'\xe8\x81\x8c\xe4\xb8\x9a')),
                ('qq', models.CharField(max_length=20, null=True, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('mobile', models.CharField(max_length=11, unique=True, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('money', models.FloatField(null=True, verbose_name=b'\xe8\xb5\x84\xe9\x87\x91', blank=True)),
                ('frozen_money', models.FloatField(unique=True, null=True, verbose_name=b'\xe5\x86\xbb\xe7\xbb\x93\xe8\xb5\x84\xe9\x87\x91', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BOSStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.IntegerField(default=0, verbose_name=b'\xe4\xb9\xb0\xe5\x8d\x96\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'0', b'Buy'), (b'1', b'Sell')])),
                ('number', models.IntegerField(verbose_name=b'\xe8\x82\xa1\xe7\xa5\xa8\xe7\xbc\x96\xe7\xa0\x81')),
                ('amount', models.IntegerField(default=100, verbose_name=b'\xe4\xb9\xb0\xe5\x8d\x96\xe6\x95\xb0\xe9\x87\x8f')),
                ('totles', models.FloatField(verbose_name=b'\xe6\x8c\x82\xe5\x8d\x95\xe9\x87\x91\xe9\xa2\x9d')),
                ('ntotle', models.FloatField(verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe9\x87\x91\xe9\xa2\x9d')),
                ('time', models.DateField(auto_now_add=True, verbose_name=b'\xe6\x8c\x82\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('state', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'0', b'deity'), (b'1', b'deal'), (b'2', b'delete'), (b'3', b'cancel')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4e70\u5356\u6302\u5355',
                'verbose_name_plural': '\u4e70\u5356\u6302\u5355',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.BooleanField(default=True, verbose_name=b'\xe4\xb9\xb0\xe5\x8d\x96\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('number', models.IntegerField(verbose_name=b'\xe8\x82\xa1\xe7\xa5\xa8\xe7\xbc\x96\xe7\xa0\x81')),
                ('amount', models.IntegerField(default=100, verbose_name=b'\xe4\xb9\xb0\xe5\x8d\x96\xe6\x95\xb0\xe9\x87\x8f')),
                ('figure', models.FloatField(verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x91\xe9\xa2\x9d')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xba\xa4\xe6\x98\x93\xe6\x97\xb6\xe9\x97\xb4')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
                'verbose_name': '\u4ea4\u6613\u8bb0\u5f55',
                'verbose_name_plural': '\u4ea4\u6613\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='DealStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dealno', models.IntegerField(verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe5\x8d\x95\xe5\x8f\xb7')),
                ('number', models.IntegerField(verbose_name=b'\xe8\x82\xa1\xe7\xa5\xa8\xe7\xbc\x96\xe7\xa0\x81')),
                ('damount', models.IntegerField(default=100, verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe6\x95\xb0\xe9\x87\x8f')),
                ('totles', models.FloatField(verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe9\x87\x91\xe9\xa2\x9d')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x88\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4')),
                ('buser', models.ForeignKey(related_name='buser', to=settings.AUTH_USER_MODEL)),
                ('suser', models.ForeignKey(related_name='suser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6210\u4ea4\u5355',
                'verbose_name_plural': '\u6210\u4ea4\u5355',
            },
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'\xe8\x82\xa1\xe7\xa5\xa8\xe7\xbc\x96\xe7\xa0\x81')),
                ('amount', models.IntegerField(default=100, verbose_name=b'\xe6\x8c\x81\xe6\x9c\x89\xe6\x95\xb0\xe9\x87\x8f')),
                ('frozen_amount', models.IntegerField(default=100, verbose_name=b'\xe5\x86\xbb\xe7\xbb\x93\xe6\x95\xb0\xe9\x87\x8f')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6301\u4ed3\u4fe1\u606f',
                'verbose_name_plural': '\u6301\u4ed3\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('callback_url', models.URLField(verbose_name=b'url\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name=b'\xe8\x82\xa1\xe7\xa5\xa8\xe7\xbc\x96\xe7\xa0\x81')),
                ('company_name', models.CharField(max_length=64, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('flow_in', models.FloatField(verbose_name=b'\xe6\x80\xbb\xe6\xb5\x81\xe5\x85\xa5')),
                ('flow_out', models.FloatField(verbose_name=b'\xe6\x80\xbb\xe6\xb5\x81\xe5\x87\xba')),
                ('impressum', models.TextField(verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u80a1\u7968\u4fe1\u606f',
                'verbose_name_plural': '\u80a1\u7968\u4fe1\u606f',
            },
        ),
    ]
