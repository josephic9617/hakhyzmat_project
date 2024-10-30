from django.contrib import admin
from main.models.service import Service
from main.admins.service import ServiceAdmin
from main.models.feature import Feature
from main.admins.feature import FeatureAdmin
from main.models.team import Team
from main.admins.team import TeamAdmin
from main.models.testimonial import Testimonial
from main.admins.testimonial import TestimonialAdmin
from main.models.blog import Blog
from main.admins.blog import BlogAdmin
from main.models.banner import Banner
from main.admins.banner import BannerAdmin
from main.models.contactus import ContactUs
from main.admins.contactus import ContactUsAdmin



admin.site.register(Service, ServiceAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(ContactUs, ContactUsAdmin)