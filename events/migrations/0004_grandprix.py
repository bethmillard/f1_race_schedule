# Generated by Django 4.2 on 2023-04-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_circuit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrandPrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand_prix_name', models.CharField(max_length=200)),
            ],
        ),
    ]
