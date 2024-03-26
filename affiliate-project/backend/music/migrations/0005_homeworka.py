# Generated by Django 5.0.2 on 2024-03-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music", "0004_statistics"),
    ]

    operations = [
        migrations.CreateModel(
            name="Homeworka",
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
                ("Homework_id", models.IntegerField()),
                ("type", models.CharField(max_length=250)),
                ("name", models.CharField(max_length=250)),
                ("start", models.CharField(max_length=250)),
                ("end", models.CharField(max_length=250)),
                ("Homework_intern_id", models.IntegerField()),
            ],
        ),
    ]