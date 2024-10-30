from django.urls import path
from main.views.home import home
from main.views.about import about
from main.views.service import service
from main.views.feature import feature
from main.views.contactus import contactus, sendmessage
from main.views.appointment import appointment
from main.views.notfound404 import notfound404
from main.views.blog import blog, blog_details
from main.views.team import team
from main.views.testimonial import testimonial

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('feature/', feature, name='feature'),
    path('contactus/', contactus, name='contactus'),
    path('sendmessage/', sendmessage, name='sendmessage'),
    path('appointment/', appointment, name='appointment'),
    path('404/', notfound404, name='404'),
    path('blog/', blog, name='blog'),
    path('blog-details/<int:pk>/', blog_details, name='blog-details'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]