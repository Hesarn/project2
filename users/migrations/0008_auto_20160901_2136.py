# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150608_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='picture',
            field=models.ImageField(default='/var/www/project2/staticimg/user.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profilePicture',
            field=models.ImageField(default='/var/www/project2/staticimg/user.png', upload_to='photo/'),
        ),
    ]
