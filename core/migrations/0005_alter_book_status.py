# Generated by Django 3.2 on 2021-06-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_refund_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('a', 'موجود'), ('c', 'عدم موجودی'), ('s', 'به زودی')], max_length=1),
        ),
    ]
