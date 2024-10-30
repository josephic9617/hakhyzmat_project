from django.shortcuts import render
from main.models.service import Service
from main.models.feature import Feature
from main.models.team import Team
from main.models.testimonial import Testimonial
from main.models.blog import Blog
from main.models.banner import Banner


def home(request):
    services = Service.objects.all()[:8]
    features = Feature.objects.all()[:8]
    teams = Team.objects.all()[:4]
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.all()[:3]
    banners = Banner.objects.all()
    data = {
        'services': services,
        'features': features,
        'teams': teams,
        'testimonials': testimonials,
        'blogs': blogs,
        'banners': banners,
    }
    return render(request, 'main/home/base.html', data)