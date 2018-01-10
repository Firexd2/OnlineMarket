from django.db import models


class Visitation(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.ip
