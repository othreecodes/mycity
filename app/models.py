from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    address = models.TextField(verbose_name='Address')
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number')
    image = models.ImageField(verbose_name='Passport')

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return self.user.first_name
