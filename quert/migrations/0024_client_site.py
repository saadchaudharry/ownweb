# Generated by Django 2.2.7 on 2021-05-01 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0023_auto_20210501_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='site',
            field=models.CharField(default='#', max_length=50),
        ),
    ]