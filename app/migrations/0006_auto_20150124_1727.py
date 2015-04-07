# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150124_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='images',
            name='assignment',
            field=models.OneToOneField(to='app.Assignment'),
            preserve_default=True,
        ),
    ]
