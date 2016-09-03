# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('roleName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(default='/static/img/user.png', upload_to='')),
                ('description', models.TextField()),
                ('averageScore', models.FloatField(default=0)),
                ('imdbLink', models.CharField(max_length=200)),
                ('profileLink', models.CharField(max_length=200, default='movieProfile.html')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('birthday', models.DateField()),
                ('profilePicture', models.ImageField(default='/static/img/user.png', upload_to='')),
                ('followerUsers', models.ManyToManyField(blank=True, to='users.MyUser')),
                ('followingUsers', models.ManyToManyField(blank=True, to='users.MyUser', related_name='following')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('notificationState', models.IntegerField(blank=True, null=True)),
                ('firstUser', models.ForeignKey(related_name='first', to='users.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('score', models.IntegerField()),
                ('body', models.TextField()),
                ('pubDate', models.DateTimeField(default=datetime.datetime.now)),
                ('film', models.ForeignKey(to='users.Film')),
                ('likeUsers', models.ManyToManyField(blank=True, to='users.MyUser', related_name='like')),
                ('user', models.ForeignKey(to='users.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(to='users.Post', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='secondUser',
            field=models.ForeignKey(related_name='second', to='users.MyUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='users.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='users.MyUser'),
        ),
        migrations.AddField(
            model_name='cast',
            name='film',
            field=models.ForeignKey(to='users.Film'),
        ),
        migrations.AddField(
            model_name='cast',
            name='person',
            field=models.ForeignKey(to='users.Person', null=True),
        ),
    ]
