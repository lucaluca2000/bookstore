# Generated by Django 3.2 on 2021-05-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210531_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='book_image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='book_image'),
        ),
    ]