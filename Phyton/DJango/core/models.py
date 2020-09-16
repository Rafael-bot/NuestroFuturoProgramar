"""
Modelo Padre
"""

#Aqui va estar modelos para todas las apps de la web.

from django.conf import settings
from django.db import models
from django.utils.timezone import now


class CommonInfo(models.Model):

    #Cuando ha sido creado
    created_at = models.DateTimeField("Created_at", default=now, blank=True)
    #Cuando ha sido mopdificado
    last_modified_at = models.DateTimeField("Last_modified_at", default=now, blank=True)
    #QUe usuario lo ha creado
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="created_by",blank=True, null=True,related_name = "%(app_label)s_%(class)s_created", on_delete=models.CASCADE)
    #QUe ultimo usuario lo ha modificado
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="last_modified_by", blank=True, null=True,  related_name="%(app_label)s_%(class)s_lastmodified", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        self.last_modified_at = now()
        super(CommonInfo, self).save(*args,**kwargs)

    class Meta:
        abstract = True
