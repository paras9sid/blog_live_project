# Generated by Django 5.0.6 on 2024-06-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallinks',
            options={'verbose_name_plural': 'social links'},
        ),
        migrations.AlterField(
            model_name='sociallinks',
            name='url',
            field=models.URLField(),
        ),
    ]
