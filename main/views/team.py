from django.shortcuts import render
from main.models.team import Team


def team(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'main/team/base.html', data)