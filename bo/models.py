from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models

class AppUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    sex_choix = (
        (0, "homme"),
        (1, "femme"),
        (2, "Not set"),
    )
    sex = models.IntegerField(choices=sex_choix, null=True, blank=True)
    location  = models.PointField(null=True, blank=True)
    online = models.BooleanField()
    lastConnexionDate = models.DateTimeField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)

    objects = models.GeoManager()

    def __unicode__(self):
       return u'%s' % (self.email)

class Cities(models.Model):
    name = models.CharField(max_length=100)
    isoCode = models.CharField(max_length=2)
    location = models.PointField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)

    objects = models.GeoManager()

    def __unicode__(self):
       return u'%s' % (self.name)

class Favorites(models.Model):
    userId = models.ForeignKey('AppUser',  db_index=True)
    citiesId = models.ForeignKey('Cities', db_index=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)
    unique_together = (("userId", "citiesId"),)
    def __unicode__(self):
        return u'%s - %s' % (self.userId,self.citiesId)
