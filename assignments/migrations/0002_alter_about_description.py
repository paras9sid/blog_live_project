# Generated by Django 5.0.6 on 2024-06-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
