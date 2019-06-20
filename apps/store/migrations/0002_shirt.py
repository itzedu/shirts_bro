# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-20 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=1)),
                ('fabric', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fabricator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_shirts', to='store.User')),
            ],
        ),
    ]
