from django.shortcuts import render
from main.models.service import Service
from main.models.feature import Feature


def service(request):
    services = Service.objects.all()
    features = Feature.objects.all()
    data = {
        'services': services,
        'features': features,
    }
    return render(request, 'main/service/base.html', data)