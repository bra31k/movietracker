# Generated by Django 2.1 on 2018-08-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('belongs_to_collection', models.CharField(max_length=999)),
                ('budget', models.CharField(max_length=999)),
                ('genres', models.CharField(max_length=999)),
                ('homepage', models.CharField(max_length=999)),
                ('id_movie', models.CharField(max_length=999)),
                ('original_title', models.CharField(max_length=999)),
                ('overview', models.CharField(max_length=999)),
            ],
        ),
    ]
