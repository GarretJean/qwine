# Generated by Django 5.0.2 on 2024-02-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qwine", "0004_cepage_cepagepercentage_vin_cepages"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cepage",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
