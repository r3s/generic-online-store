# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprices',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='productprices',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
