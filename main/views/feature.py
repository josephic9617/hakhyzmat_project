from django.shortcuts import render
from main.models.feature import Feature


def feature(request):
    features = Feature.objects.all()
    data = {
        'features': features,
    }
    return render(request, 'main/feature/base.html', data)