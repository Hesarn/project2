# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150608_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profilePicture',
            field=models.ImageField(upload_to='photo/', default='/static/img/user.png'),
        ),
    ]
