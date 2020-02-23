from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Bus(models.Model):
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    DepartureTime = models.DateTimeField(null=True,blank=True)
    slug = models.SlugField(null= True,blank=True,editable=False)

    class Meta:
        verbose_name_plural = 'buses'
        ordering = ('DepartureTime',)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify([self.origin,self.destination])
        return super().save(*args, **kwargs)


class Driver(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    age = models.IntegerField(blank=True,null=True)
    bus = models.ForeignKey(Bus,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
