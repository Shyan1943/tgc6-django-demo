# Generated by Django 2.2.6 on 2020-07-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=80),
        ),
    ]
