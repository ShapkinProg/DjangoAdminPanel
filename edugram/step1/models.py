from django.db import models
from django.urls import reverse


class vuz(models.Model):
    title = models.TextField()
    url = models.TextField()
    count_views = models.IntegerField()
    count_guests = models.IntegerField()
    VK = models.TextField()
    VK_Subs = models.IntegerField()
    VK_Video = models.IntegerField()
    YT = models.TextField()
    YT_Subs = models.IntegerField()
    YT_Views = models.IntegerField()
    TG = models.TextField()
    TG_Subs = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_vuz', kwargs={'vuzid': self.pk})

    class Meta:
        verbose_name = 'Вузы'
        verbose_name_plural = 'Вузы'
        ordering = ['id']


class Person(models.Model):
    name = models.CharField(max_length=255)
    wiki = models.TextField(null=True)
    vk = models.TextField(null=True)
    vk_subs = models.IntegerField(null=True)
    vuzs = models.ManyToManyField(vuz)
    class Meta:
        verbose_name = 'Персоналии'
        verbose_name_plural = 'Персоналии'
        ordering = ['id']