# Generated by Django 5.0.2 on 2024-02-16 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_alter_tour_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='tour.category'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='tourimages',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tour.tour'),
        ),
    ]
