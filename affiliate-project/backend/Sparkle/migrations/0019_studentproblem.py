# Generated by Django 5.0.6 on 2024-06-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sparkle', '0018_chapterkeyconcept_chapterproblem_keyconcept_problem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('answer', models.TextField()),
                ('response', models.TextField()),
                ('score', models.IntegerField()),
                ('time', models.CharField(max_length=250)),
            ],
        ),
    ]
