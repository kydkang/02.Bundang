# Generated by Django 2.1.3 on 2018-11-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181123_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Slug will be generated automatically from the title of the post', unique=True),
        ),
    ]
