# Generated by Django 5.0.2 on 2024-02-22 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qwine", "0015_alter_cave_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventaire",
            name="vin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="qwine.vin", unique=True
            ),
        ),
    ]
