# Generated by Django 3.2.4 on 2021-06-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishers',
            field=models.CharField(max_length=100, verbose_name='ناشر'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(max_length=100, null=True, verbose_name='مترجم'),
        ),
    ]