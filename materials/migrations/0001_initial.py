# Generated by Django 5.1 on 2024-09-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, upload_to='materials_files')),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
