from django.db import models
from django.conf import settings
# Create your models here.


class Corgi(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    corgies = models.IntegerField(default=0)
    corgies_per_click = models.IntegerField(default=1)
    corgies_per_second = models.IntegerField(default=0)


class Boost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="Название буста")
    count = models.IntegerField(default=0)

