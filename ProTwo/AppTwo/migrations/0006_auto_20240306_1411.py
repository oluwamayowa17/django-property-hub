# Generated by Django 3.2.5 on 2024-03-06 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0005_auto_20240306_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='property',
            name='image3',
        ),
    ]
