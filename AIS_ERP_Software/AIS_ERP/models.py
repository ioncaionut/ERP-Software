from django.db import models


#
# # Create your models here.
class AisErp(models.Model):
    objects = None
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


def post():
    return None
