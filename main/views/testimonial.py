from django.shortcuts import render
from main.models.testimonial import Testimonial


def testimonial(request):
    testimonials = Testimonial.objects.all()
    data = {
        'testimonials': testimonials,
    }
    return render(request, 'main/testimonial/base.html', data)
