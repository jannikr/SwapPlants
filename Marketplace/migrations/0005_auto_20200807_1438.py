# Generated by Django 3.0.9 on 2020-08-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0004_auto_20200807_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]