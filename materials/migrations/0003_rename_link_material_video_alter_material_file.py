# Generated by Django 5.1 on 2024-09-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_material_uploaded_at_alter_material_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='link',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(blank=True, upload_to='materials_files/'),
        ),
    ]