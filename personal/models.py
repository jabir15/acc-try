from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=200)
    full_address = models.CharField(max_length=200)
    college_district = models.CharField(max_length=140)
    college_pincode = models.PositiveIntegerField()
    college_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

