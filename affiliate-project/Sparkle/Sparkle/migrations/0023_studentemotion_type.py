# Generated by Django 5.0.6 on 2024-06-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparkle', '0022_studentemotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentemotion',
            name='type',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]