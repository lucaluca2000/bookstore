# Generated by Django 3.2 on 2021-06-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_rename_discount_book_discount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='discount_price',
            new_name='discount_percent',
        ),
        migrations.AlterField(
            model_name='order',
            name='being_delivered',
            field=models.CharField(choices=[('S', 'در صف بررسی'), ('C', 'تایید سفارش'), ('P', 'آماده سازی سفارش'), ('p', 'بسته بندی'), ('D', 'تحویل به پست'), ('c', 'تحویل مشتری')], default='S', max_length=1, verbose_name='وضعیت سفارش'),
        ),
    ]
