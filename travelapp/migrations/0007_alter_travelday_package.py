# Generated by Django 3.2.10 on 2024-03-02 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_travelday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelday',
            name='package',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='days', to='travelapp.package', verbose_name='Package'),
        ),
    ]