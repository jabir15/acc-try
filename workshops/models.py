from django.db import models

# Create your models here.

#Define the class as the table of your database
class Event(models.Model):
    #define columns of the table as members
    TYPE_EVENT = (
        ('SR', 'Seminar'),
        ('WS', 'Workshop'),
    )
    type = models.CharField(
        max_length=2,
        choices = TYPE_EVENT,
        default = 'SR',
    )
    title = models.CharField(max_length=140)
    startdate = models.DateField()
    enddate = models.DateField()
    created_at = models.DateTimeField()
    venue = models.CharField(max_length=140)
    event_details = models.TextField()  
    organiser_dept = models.CharField(max_length=140)
    organiser_college = models.CharField(max_length=140)
    organiser_district = models.CharField(max_length=140)
    organiser_state = models.CharField(max_length=140)
    organiser_pincode = models.PositiveIntegerField()

    #This is required so that you can see
    def __str__(self):
        return self.title
    