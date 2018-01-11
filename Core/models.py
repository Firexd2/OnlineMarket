from django.db import models


class Visitation(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return 'IP: %s' % self.ip

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
