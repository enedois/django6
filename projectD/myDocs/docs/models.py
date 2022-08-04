from django.db import models
import datetime
from django.utils import timezone



class methodTitle(models.Model):
    method_title = models.CharField(max_length=200)
    method_description = models.TextField()
    publicationDate = models.DateTimeField('date published')
    def __str__(self):
        return self.method_title


def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
