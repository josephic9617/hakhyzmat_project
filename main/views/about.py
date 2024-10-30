from django.shortcuts import render
from main.models.team import Team
from main.models.feature import Feature



def about(request):
    teams = Team.objects.all()
    features = Feature.objects.all()
    data = {
        'teams': teams,
        'features': features,
    }
    return render(request, 'main/about/base.html', data)
