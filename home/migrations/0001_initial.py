# Generated by Django 3.2 on 2021-04-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=45)),
                ('brief_info', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=200)),
                ('year_of_release', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('trailer_link', models.CharField(max_length=1000)),
                ('poster_link', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=2000)),
                ('run_time', models.IntegerField()),
                ('director', models.CharField(max_length=300)),
            ],
        ),
    ]
