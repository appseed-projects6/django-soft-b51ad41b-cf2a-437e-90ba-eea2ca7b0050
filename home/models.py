# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee(models.Model):

    #__Employee_FIELDS__
    employeeid = models.CharField(max_length=255, null=True, blank=True)
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    mobileno = models.CharField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Attendnace(models.Model):

    #__Attendnace_FIELDS__
    attendanceid = models.CharField(max_length=255, null=True, blank=True)
    employeeid = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    entrytime = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    #__Attendnace_FIELDS__END

    class Meta:
        verbose_name        = _("Attendnace")
        verbose_name_plural = _("Attendnace")


class Store(models.Model):

    #__Store_FIELDS__
    storeid = models.CharField(max_length=255, null=True, blank=True)
    storename = models.CharField(max_length=255, null=True, blank=True)
    storegroupid = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    #__Store_FIELDS__END

    class Meta:
        verbose_name        = _("Store")
        verbose_name_plural = _("Store")



#__MODELS__END
