# Generated by Django 3.1.2 on 2020-10-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.URLField(db_index=True, unique=True)),
                ('clicks_count', models.IntegerField(default=0)),
            ],
        ),
    ]
