# Generated by Django 5.1 on 2024-08-27 15:01

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logiks', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]