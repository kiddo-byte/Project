from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    date = models.DateTimeField(default=0)
    message = models.CharField(max_length=200, default="This is my message")


def __str__(self):
    return self.name
