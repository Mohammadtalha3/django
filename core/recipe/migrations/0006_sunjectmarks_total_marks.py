# Generated by Django 4.2.11 on 2024-05-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_subject_sunjectmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunjectmarks',
            name='Total_marks',
            field=models.IntegerField(default=0),
        ),
    ]
