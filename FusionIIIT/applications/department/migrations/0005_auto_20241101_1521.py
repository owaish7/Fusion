# Generated by Django 3.1.5 on 2024-11-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lab',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]