from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


