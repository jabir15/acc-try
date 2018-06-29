# Generated by Django 2.0.5 on 2018-06-25 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='enddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='startdate',
            field=models.DateField(),
        ),
    ]