# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150124_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='view',
            new_name='view_count',
        ),
        migrations.AddField(
            model_name='groups',
            name='description',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
    ]
