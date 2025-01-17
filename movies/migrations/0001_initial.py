# Generated by Django 5.1.3 on 2024-11-30 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('birth_city', models.CharField(max_length=100, verbose_name='Birth City')),
                ('birth_county', models.CharField(max_length=100, verbose_name='Birth County')),
                ('short_bio', models.TextField(blank=True, null=True, verbose_name='Short Bio')),
                ('role', models.CharField(max_length=50, verbose_name='Role')),
                ('nationality', models.CharField(max_length=50, verbose_name='Nationality')),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=6, verbose_name='Gender')),
                ('photo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Photo')),
                ('start_year', models.PositiveIntegerField(verbose_name='Start Year')),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='End Year')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
                'db_table': 'content.actor',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('target_audience', models.CharField(choices=[('Kids', 'Kids'), ('Teenagers', 'Teenagers'), ('Adult', 'Adult')], max_length=10, verbose_name='Target Audience')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'content.genre',
            },
        ),
        migrations.CreateModel(
            name='FilmWork',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('data_release', models.DateField(verbose_name='Release Date')),
                ('duration_min', models.PositiveIntegerField(verbose_name='Duration (minutes)')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=1, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Rating')),
                ('age_limit', models.CharField(choices=[('7+', '7+'), ('12+', '12+'), ('16+', '16+'), ('18+', '18+')], max_length=4, verbose_name='Age Limit')),
                ('type', models.CharField(max_length=50, verbose_name='Type')),
                ('language_original', models.CharField(blank=True, max_length=50, null=True, verbose_name='Original Language')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('budget', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Budget')),
                ('box_office', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Box Office')),
                ('preview', models.CharField(max_length=255, verbose_name='Preview')),
                ('total_views', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total Views')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actors', models.ManyToManyField(to='movies.actor', verbose_name='Actors')),
                ('genres', models.ManyToManyField(to='movies.genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Films',
                'db_table': 'content.filmwork',
            },
        ),
    ]
