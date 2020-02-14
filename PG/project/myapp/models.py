# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models


choices = (
    ('yes', 'YES'),
    ('no', 'NO')
)

type = (
    ('flat', 'FLAT'),
    ('pg', 'PG'),
    ('room', 'ROOM')
)

class Pg(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=255)
    contact_no = models.IntegerField()
    facility = models.CharField(max_length=255)
    furniture = models.CharField(max_length=255, choices=choices, default='no')
    food = models.CharField(max_length=255, choices=choices, default='no')
    rent = models.IntegerField()
    type = models.CharField(max_length=255, choices=type, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pg"
        verbose_name = "PG"
        managed = True


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact_no = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.address

    class Meta:
        db_table = "profile"
        verbose_name = "PROFILE"
        managed = True
