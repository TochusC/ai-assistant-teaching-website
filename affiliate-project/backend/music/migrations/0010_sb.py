# Generated by Django 5.0.2 on 2024-03-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0009_catalogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="sb",
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
                ("Course_id", models.IntegerField()),
                ("Design_id", models.IntegerField()),
                ("Statistics_id", models.IntegerField()),
            ],
        ),
    ]
