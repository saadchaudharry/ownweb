# Generated by Django 2.2.7 on 2020-05-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('subtitle', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('site', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_no',
            field=models.IntegerField(max_length=120),
        ),
    ]
