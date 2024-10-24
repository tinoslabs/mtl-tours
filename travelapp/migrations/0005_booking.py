# Generated by Django 3.2.10 on 2024-01-26 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_auto_20240121_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('num_people', models.IntegerField()),
                ('message', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.category')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.package')),
            ],
        ),
    ]
