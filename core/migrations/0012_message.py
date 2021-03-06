# Generated by Django 3.2 on 2021-06-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_address_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('username', models.CharField(max_length=30)),
                ('password1', models.CharField(max_length=40)),
                ('password2', models.CharField(max_length=40)),
                ('contact', models.IntegerField(max_length=15)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
