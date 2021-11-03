from django.db import models


class SigningUp(models.Model):
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(
        max_length=213, null=True, blank=True, default="")
    email = models.CharField(max_length=213, null=True, blank=True, default="")
    password = models.CharField(max_length=213, null=True, blank=True, default="")
    username = models.CharField(
        max_length=213, null=True, blank=True, default="")
    gender = models.CharField(max_length=10, null=True, blank=True, default="")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.fullname + ' as ' + self.username
