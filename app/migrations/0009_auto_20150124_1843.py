# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_assignment_pic_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='pic_count',
            new_name='image_count',
        ),
    ]
