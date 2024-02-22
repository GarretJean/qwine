# Generated by Django 5.0.2 on 2024-02-22 09:19

import django.core.validators
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("appelation", models.CharField(max_length=100)),
                ("volume", models.PositiveIntegerField()),
                (
                    "pays",
                    django_countries.fields.CountryField(db_index=True, max_length=2),
                ),
                ("region", models.CharField(db_index=True, max_length=100)),
                (
                    "degree",
                    models.PositiveSmallIntegerField(
                        db_index=True,
                        validators=[django.core.validators.MaxValueValidator(100)],
                    ),
                ),
                (
                    "couleur",
                    models.CharField(
                        choices=[
                            ("BL", "Blanc"),
                            ("RO", "Rouge"),
                            ("RS", "Rosé"),
                            ("OR", "Orange"),
                        ]
                    ),
                ),
            ],
        ),
    ]
