# Generated by Django 2.2.7 on 2020-06-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0009_auto_20200607_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='list2',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='list3',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='list4',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='list5',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='list6',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='list',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
    ]