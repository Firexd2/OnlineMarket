from django.db import models


class Visitation(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return 'IP: %s' % self.ip

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'


class SlideBanner(models.Model):
    slide = models.ImageField('Загрузка нового слайда', upload_to='banner',
                              help_text='ВНИМАНИЕ! Для корректного отображения необходимо загружать изображения 760x350')

    def __str__(self):
        return str(self.slide)

    class Meta:
        verbose_name = 'Слайд баннера'
        verbose_name_plural = 'Слайды баннера'
