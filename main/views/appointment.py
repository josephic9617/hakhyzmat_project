from django.shortcuts import render


def appointment(request):
    return render(request, 'main/appointment/base.html')