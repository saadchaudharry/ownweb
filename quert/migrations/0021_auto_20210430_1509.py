# Generated by Django 2.2.7 on 2021-04-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0020_auto_20210425_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='service_photos/IMG1'),
        ),
        migrations.AddField(
            model_name='price',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='service_photos/IMG2'),
        ),
        migrations.AddField(
            model_name='price',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='service_photos/IMG3'),
        ),
    ]
