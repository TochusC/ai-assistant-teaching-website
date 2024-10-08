# Generated by Django 5.0.6 on 2024-07-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparkle', '0025_studentmental'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('tittle', models.CharField(max_length=250)),
                ('sender', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('tittle', models.CharField(max_length=250)),
                ('sender', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tittle', models.CharField(max_length=250)),
                ('sender', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
            ],
        ),
    ]
