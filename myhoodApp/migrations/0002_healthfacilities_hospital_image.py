# Generated by Django 3.2.7 on 2021-09-23 20:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthfacilities',
            name='hospital_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Hospital Image'),
        ),
    ]
