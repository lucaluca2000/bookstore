# Generated by Django 3.2 on 2021-05-31 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210531_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='being_delivered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='received',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_granted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='refund_requested',
        ),
    ]