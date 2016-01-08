# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='image',
            field=models.ImageField(null=True, upload_to=shop.models.unique_image_name),
        ),
    ]
