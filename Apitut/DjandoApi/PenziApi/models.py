from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    level_of_edu = models.CharField(max_length=100, null=True, blank=True)
    profesion = models.CharField(max_length=100, null=True, blank=True)
    marital_stat = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    ethnicity = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=100)
    receipient = models.CharField(max_length=100)
    message_txt = models.TextField()
    response = models.CharField(max_length=255, blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_txt
