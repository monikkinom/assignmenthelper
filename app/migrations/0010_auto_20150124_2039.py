# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150124_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='rating',
            new_name='view',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=b'user_content'),
            preserve_default=True,
        ),
    ]
