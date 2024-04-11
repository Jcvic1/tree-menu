from django.db import models

# Create your models here.


class Menu(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.title