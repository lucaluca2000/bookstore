# Generated by Django 3.2 on 2021-06-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210620_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street_address',
            field=models.CharField(max_length=250, verbose_name='آدرس خیابان'),
        ),
    ]