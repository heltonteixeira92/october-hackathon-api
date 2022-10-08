from django.db import models


class Advocates(models.Model):
    name = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to='img')
    short_bio = models.CharField(max_length=150)
    long_bio = models.TextField()
    advocate_years_exp = models.IntegerField(default=1)


class Company(models.Model):
    name = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to='img')
    summary = models.TextField()
