# Generated by Django 2.2.7 on 2021-04-25 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0018_auto_20200722_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='service_photos')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'case study'},
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=999),
        ),
    ]