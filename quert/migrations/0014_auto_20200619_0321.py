# Generated by Django 2.2.7 on 2020-06-18 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0013_auto_20200619_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ema',
            field=models.CharField(blank=True, default='abd', max_length=120, null=True),
        ),
    ]
