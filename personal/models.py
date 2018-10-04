from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=200)
    full_address = models.CharField(max_length=200)
    college_district = models.CharField(max_length=140)
    college_pincode = models.PositiveIntegerField()
    college_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Update(models.Model):
    TYPE_UPDATE = (
        ('DHE', 'Related to DHE'),
        ('UGC', 'Related to UGC'),
        ('OTH', 'Others')
    )
    update_type = models.CharField(
        max_length=3,
        choices = TYPE_UPDATE,
        default = 'DHE'
    )
    title = models.CharField(max_length=140)
    message = models.CharField(max_length=500)
    message_url = models.URLField(blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def is_new(self):
        now = timezone.now().date()
        cdate = self.created_at.date()+timedelta(7,0,0)
        return cdate>=now



