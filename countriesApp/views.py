from django.shortcuts import render, get_object_or_404
from .models import Country, Measurement
from django.core.serializers.json import DjangoJSONEncoder
import json

def country_detail(request, country_code):
    country = get_object_or_404(Country, code=country_code.upper())
    measurements = Measurement.objects.filter(country=country).order_by('year')

    years = [m.year for m in measurements]
    values = [m.value if m.value is not None else None for m in measurements]

    return render(request, 'countriesApp/country_detail.html', {
        'country': country,
        'measurements': measurements,
        'years': json.dumps(years, cls=DjangoJSONEncoder),
        'values': json.dumps(values, cls=DjangoJSONEncoder)
    })
