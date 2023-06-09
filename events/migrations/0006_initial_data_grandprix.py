# Generated by Django 4.2 on 2023-04-18 14:55

from django.db import migrations

input = [
    "Formula 1 Gulf Air Bahrain Grand Prix 2023",
    "Formula 1 STC Saudi Arabian Grand Prix 2023",
    "Formula 1 Rolex Australian Grand Prix 2023",
    "Formula 1 Azerbaijan Grand Prix 2023",
    "Formula 1 CRYPTO.COM Miami Grand Prix 2023",
    "Formula 1 Qatar Airways Gran Premio Del Made In Italy E Dell'Emilia-Romagna 2023",
    "Formula 1 Grand Prix De Monaco 2023",
    "Formula 1 AWS Gran Premio De Espana 2023",
    "Formula 1 Pirelli Grand Prix Du Canada 2023",
    "Formula 1 Grosser Preis Von Osterreich",
    "Formula 1 Aramco British Grand Prix 2023",
    "Formula 1 Qatar Airwars Hungarian Grand Prix 2023",
    "Formula 1 MSC Cruises Belgium Grand Prix 2023",
    "Formula 1 Heineken Dutch Grand Prix 2023",
    "Formula 1 Pirelli Gran Premio D'Italia 2023",
    "Formula 1 Singapore Airlines Singapore Grand Prix 2023",
    "Formula 1 Lenovo Japanese Grand Prix 2023",
    "Formula 1 Qatar Airways Qatar Grand Prix 2023",
    "Formula 1 Lenovo United States Grand Prix 2023",
    "Formula 1 Gran Premio De La Ciudad De Mexico 2023",
    "Formula 1 Rolex Grande Premio De Sao Paulo 2023",
    "Formula 1 Heiniken Silver Las Vegas Grand Prix 2023",
    "Formula 1 Etihad Airways Abu Dhabi Grand Prix 2023",
]

def forwards(apps, *args, **kwargs):
    GrandPrix = apps.get_model("events", "GrandPrix")

    for name in input:
        GrandPrix.objects.create(grand_prix_name=name)

def backwards(apps, *args, **kwargs):
    GrandPrix = apps.get_model("events", "GrandPrix")

    GrandPrix.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_initial_data_location'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
