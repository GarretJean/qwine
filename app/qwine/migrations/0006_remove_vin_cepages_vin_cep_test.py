# Generated by Django 5.0.2 on 2024-02-22 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qwine", "0005_alter_cepage_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vin",
            name="cepages",
        ),
        migrations.AddField(
            model_name="vin",
            name="cep_test",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="qwine.cepage",
            ),
        ),
    ]
