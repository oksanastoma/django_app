from django.db import models


class Contact(models.Model):
    phone_number = models.CharField(max_length=40)
    email = models.EmailField()
    name = models.CharField(max_length=200)
