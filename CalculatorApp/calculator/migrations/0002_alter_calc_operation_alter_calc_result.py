# Generated by Django 4.0.5 on 2022-06-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calc',
            name='operation',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='calc',
            name='result',
            field=models.CharField(max_length=200),
        ),
    ]
