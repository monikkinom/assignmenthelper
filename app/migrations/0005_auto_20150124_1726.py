# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_assignment_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='images',
        ),
        migrations.AddField(
            model_name='images',
            name='assignment',
            field=models.OneToOneField(null=True, to='app.Assignment'),
            preserve_default=True,
        ),
    ]
