from django.db import models


class User(models.Model):
    userName = models.CharField(max_length=20)
    accountName = models.CharField(max_length=20)
    emailAddr = models.EmailField(max_length=50)
    userPasswd = models.CharField(max_length=20)

    def __unicode__(self):
        return self.userName
