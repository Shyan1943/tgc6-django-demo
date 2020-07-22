# Generated by Django 2.2.6 on 2020-07-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.Genre'),
            preserve_default=False,
        ),
    ]
