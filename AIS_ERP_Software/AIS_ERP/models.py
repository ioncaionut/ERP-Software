from django.contrib import auth
from django.db import models
from django.utils import timezone
#####################################################
# # Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


    objects = None
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


def post():
    return None
