# Generated by Django 2.2.7 on 2020-06-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0015_remove_contact_ema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
