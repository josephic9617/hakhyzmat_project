from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'