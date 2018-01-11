from django.db import models


class Visitation(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % self.ip
