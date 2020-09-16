from django.db import models

from core.models import CommonInfo


class bar(CommonInfo):
    name = models.CharField('Name', max_length=50)
    capacidad = models.IntegerField('Capacidad', default = 0)