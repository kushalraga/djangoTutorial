# Generated by Django 5.2.1 on 2025-05-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
