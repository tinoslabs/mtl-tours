# Generated by Django 3.2.10 on 2024-03-07 21:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0023_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]