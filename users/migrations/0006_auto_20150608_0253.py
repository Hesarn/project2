# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150608_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profilePicture',
            field=models.FileField(default='/static/img/user.png', upload_to='/photo'),
        ),
    ]
