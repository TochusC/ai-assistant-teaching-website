# Generated by Django 5.0.6 on 2024-06-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('school', models.CharField(max_length=250)),
            ],
        ),
    ]