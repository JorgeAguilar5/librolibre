# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 06:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='titulo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='libros_publicados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='libro',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]