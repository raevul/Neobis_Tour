# Generated by Django 5.0.2 on 2024-02-21 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tour.tour'),
        ),
    ]