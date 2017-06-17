# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Foreman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location1', models.CharField(max_length=20)),
                ('qualification', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='KYM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location2', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]