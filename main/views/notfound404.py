from django.shortcuts import render


def notfound404(request, exception):
    return render(request, 'main/notfound404/base.html')