# Generated by Django 5.1.6 on 2025-03-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_id', models.CharField(max_length=100)),
                ('Course_name', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
            ],
        ),
    ]
