# Generated by Django 5.0.2 on 2024-02-15 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='Tour main image', verbose_name='Tour image')),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tour.category')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='TourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to='Tour other images', verbose_name='Other images')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='tour.tour')),
            ],
            options={
                'verbose_name': 'Tour image',
                'verbose_name_plural': 'Tour images',
            },
        ),
    ]
