from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    address = models.TextField(verbose_name='Address')
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number')
    image = models.ImageField(verbose_name='Passport')

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return self.user.first_name


class Place(models.Model):
    owner = models.ForeignKey(User, related_name='owner')
    name = models.CharField(max_length=256, verbose_name='Name of Place')
    location = models.TextField(verbose_name='Location')
    choices = (
        ('Shop', 'Shop'),
        ('Cinema', 'Cinema'),
        ('Cafe', 'Cafe'),
        ('Club', 'Club'),
        ('Sport', 'Sport'),
        ('Bank', 'Bank'), ('Showplace', 'Showplace'), ('Park', 'Park')
    )
    place_type = models.CharField(max_length=256, verbose_name='Type')
    image = models.ImageField(verbose_name='Image')
