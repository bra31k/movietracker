# Generated by Django 2.1 on 2018-08-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.CharField(max_length=999),
        ),
    ]
