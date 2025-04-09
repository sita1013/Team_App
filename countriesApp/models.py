from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

    def get_all_countries():
        return Country.objects.all()

    def get_by_name(country_name):
        return Country.objects.filter(name=country_name)

class Indicator(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    


class Measurement(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('country', 'indicator', 'year')

    def __str__(self):
        return f"{self.country} - {self.indicator} - {self.year}: {self.value}"
