# Generated by Django 2.2.7 on 2021-04-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0021_auto_20210430_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='head',
            field=models.CharField(default='thsi heading', max_length=50),
        ),
    ]
