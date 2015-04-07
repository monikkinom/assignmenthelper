# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150124_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='pic_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
