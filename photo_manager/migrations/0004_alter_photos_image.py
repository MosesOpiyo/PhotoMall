# Generated by Django 3.2.8 on 2021-10-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_manager', '0003_rename_image_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
