from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'