# Generated by Django 2.0.5 on 2018-06-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('venue', models.CharField(max_length=140)),
                ('event_details', models.TextField()),
                ('organiser_dept', models.CharField(max_length=140)),
                ('organiser_college', models.CharField(max_length=140)),
                ('organiser_district', models.CharField(max_length=140)),
                ('organiser_state', models.CharField(max_length=140)),
                ('organiser_pincode', models.PositiveIntegerField()),
            ],
        ),
    ]
