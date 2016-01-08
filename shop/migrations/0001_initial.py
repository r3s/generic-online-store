# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=128)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('date_submitted', models.DateTimeField(null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_incl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('price_currency', models.CharField(max_length=16)),
                ('date_created', models.DateTimeField()),
                ('basket', models.ForeignKey(to='shop.Basket')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('track_stock', models.BooleanField()),
                ('requires_shipping', models.BooleanField()),
                ('serial_number', models.CharField(max_length=128)),
                ('product_code', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('parent_slug', models.SlugField()),
                ('depth', models.PositiveSmallIntegerField()),
                ('parent', models.ForeignKey(related_name='parent_for', to='shop.ProductCategories', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=128)),
                ('display_order', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('selling_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('discount_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('reorder_point', models.PositiveSmallIntegerField()),
                ('reorder_quantity', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='VendorAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(max_length=255)),
                ('line3', models.CharField(max_length=255)),
                ('line4', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='vendoraddress',
            name='vendor',
            field=models.ForeignKey(to='shop.Vendors'),
        ),
        migrations.AddField(
            model_name='productstock',
            name='vendor',
            field=models.ForeignKey(to='shop.Vendors'),
        ),
        migrations.AddField(
            model_name='productprices',
            name='vendor',
            field=models.ForeignKey(to='shop.Vendors'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='shop.ProductCategories'),
        ),
        migrations.AddField(
            model_name='basketline',
            name='product',
            field=models.ForeignKey(to='shop.Product'),
        ),
    ]
