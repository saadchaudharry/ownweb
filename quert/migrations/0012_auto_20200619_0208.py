# Generated by Django 2.2.7 on 2020-06-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0011_auto_20200607_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geeks_field', models.GenericIPAddressField()),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='ema',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
