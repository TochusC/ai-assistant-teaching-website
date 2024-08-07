# Generated by Django 5.0.6 on 2024-06-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparkle', '0016_studentcourse_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentassignment',
            name='answer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentassignment',
            name='response',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentassignment',
            name='score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentassignment',
            name='time',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
