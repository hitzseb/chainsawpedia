# Generated by Django 3.2.18 on 2023-05-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='appearance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='devil_form',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='fiend_form',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='human_form',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='hybrid_form',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='personality',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='powers_and_abilities',
            field=models.TextField(blank=True, null=True),
        ),
    ]