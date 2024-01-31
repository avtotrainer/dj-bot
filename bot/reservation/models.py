from django.db import models

# Create your models here.

class BotSetting(models.Model):
    name = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PersonStatus(models.Model):
    status = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.status

class Person(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    roles = models.ManyToManyField(Role, blank=True)
    person_status = models.ForeignKey(PersonStatus, on_delete=models.SET_NULL, null=True, blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.name
