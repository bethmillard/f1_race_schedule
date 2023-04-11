# Generated by Django 4.2 on 2023-04-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='circuit_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.location'),
            preserve_default=False,
        ),
    ]
