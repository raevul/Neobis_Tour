# Generated by Django 5.0.2 on 2024-03-04 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_userprofile_phone'),
        ('reserve', '0006_alter_reserve_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reserve',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve', to='reserve.reserve'),
        ),
    ]