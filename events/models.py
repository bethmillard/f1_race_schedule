from django.db import models

class Location(models.Model):
    circuit_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.circuit_name} - {self.city}, {self.country}"

class GrandPrix(models.Model):
    grand_prix_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.grand_prix_name}"

class Event(models.Model):
    event = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    circuit_name = models.ForeignKey(Location, on_delete=models.CASCADE, default=48)
    grand_prix_name = models.ForeignKey(GrandPrix, on_delete=models.CASCADE, default=24)

    def __str__(self) -> str:
        return f"{self.circuit_name}: {self.event} - {self.start_time}, {self.date}"
