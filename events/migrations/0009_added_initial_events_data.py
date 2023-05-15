# Generated by Django 4.2 on 2023-05-09 10:05

from django.db import migrations
# event, date, start_time, duration
bahrain_events = [
    ("Practice Session 1", "2023-03-03", "14:30", 1),
    ("Practice Session 2", "2023-03-03", "18:00", 1),
    ("Practice Session 3", "2023-03-04", "14:30", 1),
    ("Qualifying Session", "2023-03-04", "18:00", 1),
    ("Grand Prix", "2023-03-05", "18:00", 2),
]

saudi_events = [
    ("Practice Session 1", "2023-03-17", "16:30", 1),
    ("Practice Session 2", "2023-03-17", "20:00", 1),
    ("Practice Session 3", "2023-03-18", "16:30", 1),
    ("Qualifying Session", "2023-03-18", "20:00", 1),
    ("Grand Prix", "2023-03-19", "20:00", 2),
]

aus_events = [
    ("Practice Session 1", "2023-03-31", "12:30", 1),
    ("Practice Session 2", "2023-03-31", "16:00", 1),
    ("Practice Session 3", "2023-04-01", "12:30", 1),
    ("Qualifying Session", "2023-04-01", "16:00", 1),
    ("Grand Prix", "2023-04-02", "15:00", 2),
]

azerbaijan_events = [
    ("Practice Session 1", "2023-04-28", "10:30", 1),
    ("Qualifying Session", "2023-04-28", "14:00", 1),
    ("Sprint Shootout", "2023-04-29", "9:30", 0.45),
    ("Sprint Race", "2023-04-29", "14:30", 0.30),
    ("Grand Prix", "2023-04-30", "12:00", 2),
]

miami_events = [
    ("Practice Session 1", "2023-05-05", "19:00", 1),
    ("Practice Session 2", "2023-05-05", "22:30", 1),
    ("Practice Session 3", "2023-05-06", "17:30", 1),
    ("Qualifying Session", "2023-05-06", "21:00", 1),
    ("Grand Prix", "2023-05-07", "20:30", 2),
]

imola_events = [
    ("Practice Session 1", "2023-05-19", "12:30", 1),
    ("Practice Session 2", "2023-05-19", "16:00", 1),
    ("Practice Session 3", "2023-05-20", "11:30", 1),
    ("Qualifying Session", "2023-05-20", "15:00", 1),
    ("Grand Prix", "2023-05-21", "14:00", 2),
]

monaco_events = [
    ("Practice Session 1", "2023-05-26", "12:30:00", 1),
    ("Practice Session 2", "2023-05-26", "16:00:00", 1),
    ("Practice Session 3", "2023-05-27", "11:30:00", 1),
    ("Qualifying Session", "2023-05-27", "15:00:00", 1),
    ("Grand Prix", "2023-05-28", "14:00:00", 2),
]

spain_events = [
    ("Practice Session 1", "2023-05-26", "12:30:00", 1),
    ("Practice Session 2", "2023-05-26", "16:00:00", 1),
    ("Practice Session 3", "2023-05-27", "11:30:00", 1),
    ("Qualifying Session", "2023-05-27", "15:00:00", 1),
    ("Grand Prix", "2023-05-28", "14:00:00", 2),
]

canada_events = [
    ("Practice Session 1", "2023-06-16", "18:30:00", 1),
    ("Practice Session 2", "2023-06-16", "22:00:00", 1),
    ("Practice Session 3", "2023-06-17", "17:30:00", 1),
    ("Qualifying Session", "2023-06-17", "21:00:00", 1),
    ("Grand Prix", "2023-06-18", "19:00:00", 2),
]

austria_events = [
    ("Practice Session 1", "2023-06-30", "12:30:00", 1),
    ("Qualifying Session", "2023-06-30", "16:00:00", 1),
    ("Sprint Shootout", "2023-07-01", "11:00:00", 0.45),
    ("Sprint Race", "2023-07-01", "15:30:00", 0.30),
    ("Grand Prix", "2023-07-02", "14:00:00", 2),
]

silverstone_events = [
    ("Practice Session 1", "2023-07-07", "12:30:00", 1),
    ("Practice Session 2", "2023-07-07", "16:00:00", 1),
    ("Practice Session 3", "2023-07-08", "11:30:00", 1),
    ("Qualifying Session", "2023-07-08", "15:00:00", 1),
    ("Grand Prix", "2023-07-09", "15:00:00", 2)
]

hungary_events = [
    ("Practice Session 1", "2023-07-21", "12:30:00", 1),
    ("Practice Session 2", "2023-07-21", "16:00:00", 1),
    ("Practice Session 3", "2023-07-22", "11:30:00", 1),
    ("Qualifying Session", "2023-07-22", "15:00:00", 1),
    ("Grand Prix", "2023-07-23", "14:00:00", 2),
]

spa_events = [
    ("Practice Session 1", "2023-07-28", "12:30:00", 1),
    ("Qualifying Session", "2023-07-28", "16:00:00", 1),
    ("Sprint Shootout", "2023-07-29", "11:00:00", 0.45),
    ("Sprint Race", "2023-07-29", "15:30:00", 0.30),
    ("Grand Prix", "2023-07-30", "14:00:00", 2),
]

dutch_events = [
    ("Practice Session 1", "2023-08-25", "11:30:00", 1),
    ("Practice Session 2", "2023-08-25", "15:00:00", 1),
    ("Practice Session 3", "2023-08-26", "10:30:00", 1),
    ("Qualifying Session", "2023-08-26", "14:00:00", 1),
    ("Grand Prix", "2023-08-27", "14:00:00", 2),
]

monza_events = [
    ("Practice Session 1", "2023-09-01", "12:30:00", 1),
    ("Practice Session 2", "2023-09-01", "16:00:00", 1),
    ("Practice Session 3", "2023-09-02", "11:30:00", 1),
    ("Qualifying Session", "2023-09-02", "15:00:00", 1),
    ("Grand Prix", "2023-09-03", "14:00:00", 2),
]

singapore_events = [
    ("Practice Session 1", "2023-09-15", "10:30:00", 1),
    ("Practice Session 2", "2023-09-15", "14:00:00", 1),
    ("Practice Session 3", "2023-09-16", "10:30:00", 1),
    ("Qualifying Session", "2023-09-16", "14:00:00", 1),
    ("Grand Prix", "2023-09-17", "13:00:00", 2),
]

japan_events = [
    ("Practice Session 1", "2023-09-22", "3:30:00", 1),
    ("Practice Session 2", "2023-09-22", "7:00:00", 1),
    ("Practice Session 3", "2023-09-23", "3:30:00", 1),
    ("Qualifying Session", "2023-09-23", "7:00:00", 1),
    ("Grand Prix", "2023-09-24", "6:00:00", 2),
]

qatar_events = [
    ("Practice Session 1", "2023-10-06", "14:30:00", 1),
    ("Qualifying Session", "2023-10-06", "18:00:00", 1),
    ("Sprint Shootout", "2023-10-07", "14:00:00", 0.45),
    ("Sprint Race", "2023-10-07", "18:30:00", 0.30),
    ("Grand Prix", "2023-10-08", "18:00:00", 2)
]

cota_events = [
    ("Practice Session 1", "2023-10-20", "18:30:00", 1),
    ("Qualifying Session", "2023-10-20", "22:00:00", 1),
    ("Sprint Shootout", "2023-10-21", "18:30:00", 0.45),
    ("Sprint Race", "2023-10-21", "23:00:00", 0.30),
    ("Grand Prix", "2023-10-22", "20:00:00", 2),
]

mexico_events = [
    ("Practice Session 1", "2023-10-27", "19:30:00", 1),
    ("Practice Session 2", "2023-10-27", "23:00:00", 1),
    ("Practice Session 3", "2023-10-28", "18:30:00", 1),
    ("Qualifying Session", "2023-10-28", "22:00:00", 1),
    ("Grand Prix", "2023-10-29", "20:00:00", 2),
]

brazil_events = [
    ("Practice Session 1", "2023-11-03", "14:30:00", 1),
    ("Qualifying Session", "2023-11-03", "18:00:00", 1),
    ("Sprint Shootout", "2023-11-04", "14:00:00", 0.45),
    ("Sprint Race", "2023-11-04", "18:30:00", 0.30),
    ("Grand Prix", "2023-11-05", "17:00:00", 2),
]

vegas_events = [
    ("Practice Session 1", "2023-11-17", "4:30:00", 1),
    ("Practice Session 2", "2023-11-17", "8:00:00", 1),
    ("Practice Session 3", "2023-11-18", "4:30:00", 1),
    ("Qualifying Session", "2023-11-18", "8:00:00", 1),
    ("Grand Prix", "2023-11-19", "6:00:00", 2),
]

abu_dhabi_events = [
    ("Practice Session 1", "2023-11-24", "9:30:00", 1),
    ("Practice Session 2", "2023-11-24", "13:00:00", 1),
    ("Practice Session 3", "2023-11-25", "10:30:00", 1),
    ("Qualifying Session", "2023-11-25", "14:00:00", 1),
    ("Grand Prix", "2023-11-26", "13:00:00", 2),
]

def forwards(apps, *args, **kwargs):
    Event = apps.get_model("events", "Event")
    Location = apps.get_model("events", "Location")
    GrandPrix = apps.get_model("events", "GrandPrix")


    # Bahrain
    bahrain_location = Location.objects.get(id=25)
    bahrain_prix = GrandPrix.objects.get(id=1)
    for event, date, start_time, duration in bahrain_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=bahrain_location,
            grand_prix_name=bahrain_prix
        )

    # Saudi
    saudi_location = Location.objects.get(id=26)
    saudi_prix = GrandPrix.objects.get(id=2)
    for event, date, start_time, duration in saudi_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=saudi_location,
            grand_prix_name=saudi_prix
        )

    # Aus
    aus_location = Location.objects.get(id=27)
    aus_prix = GrandPrix.objects.get(id=3)
    for event, date, start_time, duration in aus_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=aus_location,
            grand_prix_name=aus_prix
        )

    # Azerbaijan
    azerbaijan_location = Location.objects.get(id=28)
    azerbaijan_prix = GrandPrix.objects.get(id=4)
    for event, date, start_time, duration in azerbaijan_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=azerbaijan_location,
            grand_prix_name=azerbaijan_prix
        )

    # Miami
    miami_location = Location.objects.get(id=29)
    miami_prix = GrandPrix.objects.get(id=5)
    for event, date, start_time, duration in miami_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=miami_location,
            grand_prix_name=miami_prix
        )

    # Imola
    imola_location = Location.objects.get(id=30)
    imola_prix = GrandPrix.objects.get(id=6)
    for event, date, start_time, duration in imola_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=imola_location,
            grand_prix_name=imola_prix
        )

    # Monaco
    monaco_location = Location.objects.get(id=31)
    monaco_prix = GrandPrix.objects.get(id=7)
    for event, date, start_time, duration in monaco_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=monaco_location,
            grand_prix_name=monaco_prix
        )

    # Spain
    spain_location = Location.objects.get(id=32)
    spain_prix = GrandPrix.objects.get(id=8)
    for event, date, start_time, duration in spain_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=spain_location,
            grand_prix_name=spain_prix
        )

    # Canada
    canada_location = Location.objects.get(id=33)
    canada_prix = GrandPrix.objects.get(id=9)
    for event, date, start_time, duration in canada_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=canada_location,
            grand_prix_name=canada_prix
        )

    # Austria
    austria_location = Location.objects.get(id=34)
    austria_prix = GrandPrix.objects.get(id=10)
    for event, date, start_time, duration in austria_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=austria_location,
            grand_prix_name=austria_prix
        )

    # Silverstone
    silverstone_location = Location.objects.get(id=35)
    silverstone_prix = GrandPrix.objects.get(id=11)
    for event, date, start_time, duration in silverstone_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=silverstone_location,
            grand_prix_name=silverstone_prix
        )

    # Hungary
    hungary_location = Location.objects.get(id=36)
    hungary_prix = GrandPrix.objects.get(id=12)
    for event, date, start_time, duration in hungary_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=hungary_location,
            grand_prix_name=hungary_prix
        )

    # Spa
    spa_location = Location.objects.get(id=37)
    spa_prix = GrandPrix.objects.get(id=13)
    for event, date, start_time, duration in spa_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=spa_location,
            grand_prix_name=spa_prix
        )

    # Netherlands
    dutch_location = Location.objects.get(id=38)
    dutch_prix = GrandPrix.objects.get(id=14)
    for event, date, start_time, duration in dutch_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=dutch_location,
            grand_prix_name=dutch_prix
        )

    # Monza
    monza_location = Location.objects.get(id=39)
    monza_prix = GrandPrix.objects.get(id=15)
    for event, date, start_time, duration in monza_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=monza_location,
            grand_prix_name=monza_prix
        )

    # Singapore
    singapore_location = Location.objects.get(id=40)
    singapore_prix = GrandPrix.objects.get(id=16)
    for event, date, start_time, duration in singapore_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=singapore_location,
            grand_prix_name=singapore_prix
        )

    # Japan
    japan_location = Location.objects.get(id=41)
    japan_prix = GrandPrix.objects.get(id=17)
    for event, date, start_time, duration in japan_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=japan_location,
            grand_prix_name=japan_prix
        )

    # Qatar
    qatar_location = Location.objects.get(id=42)
    qatar_prix = GrandPrix.objects.get(id=18)
    for event, date, start_time, duration in qatar_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=qatar_location,
            grand_prix_name=qatar_prix
        )

    # COTA
    cota_location = Location.objects.get(id=43)
    cota_prix = GrandPrix.objects.get(id=19)
    for event, date, start_time, duration in cota_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=cota_location,
            grand_prix_name=cota_prix
        )

    # Mexico
    mexico_location = Location.objects.get(id=44)
    mexico_prix = GrandPrix.objects.get(id=20)
    for event, date, start_time, duration in mexico_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=mexico_location,
            grand_prix_name=mexico_prix
        )

    # Brazil
    brazil_location = Location.objects.get(id=45)
    brazil_prix = GrandPrix.objects.get(id=21)
    for event, date, start_time, duration in brazil_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=brazil_location,
            grand_prix_name=brazil_prix
        )

    # Vegas
    vegas_location = Location.objects.get(id=46)
    vegas_prix = GrandPrix.objects.get(id=22)
    for event, date, start_time, duration in vegas_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=vegas_location,
            grand_prix_name=vegas_prix
        )

    # Abu Dhabi
    abu_dhabi_location = Location.objects.get(id=47)
    abu_dhabi_prix = GrandPrix.objects.get(id=23)
    for event, date, start_time, duration in abu_dhabi_events:
        Event.objects.create(
            event=event,
            date=date,
            start_time=start_time,
            duration=duration,
            circuit_name=abu_dhabi_location,
            grand_prix_name=abu_dhabi_prix
        )

def backwards(apps, *args, **kwargs):
    Event = apps.get_model("events", "Event")

    Event.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_grand_prix_name_alter_event_circuit_name'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]