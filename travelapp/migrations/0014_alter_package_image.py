# Generated by Django 3.2.10 on 2024-03-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0013_auto_20240303_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]