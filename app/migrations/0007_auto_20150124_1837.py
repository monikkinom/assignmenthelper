# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150124_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='group',
            field=models.ForeignKey(to='app.Groups'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='images',
            name='assignment',
            field=models.ForeignKey(to='app.Assignment'),
            preserve_default=True,
        ),
    ]
