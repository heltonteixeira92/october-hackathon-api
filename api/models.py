from django.db import models


class Advocates(models.Model):
    name = models.CharField(max_length=250)
    profile_pic = models.ImageField(upload_to='image/profile', default='image/default.jpg')
    short_bio = models.CharField(max_length=150)
    long_bio = models.TextField()
    advocate_years_exp = models.IntegerField(default=1)
    company = models.ForeignKey('Company', on_delete=models.PROTECT)
    links = models.ForeignKey('Links', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='image/logo', default='image/default.jpg')
    summary = models.TextField()

    def __str__(self):
        return self.name


class Links(models.Model):
    youtube = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
