# Generated by Django 3.2.18 on 2023-05-23 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volumes', '0002_auto_20230523_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volume',
            name='arc',
        ),
    ]
