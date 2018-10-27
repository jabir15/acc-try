# Generated by Django 2.0.5 on 2018-10-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20180721_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_type', models.CharField(choices=[('DHE', 'Related to DHE'), ('UGC', 'Related to UGC'), ('OTH', 'Others')], default='DHE', max_length=3)),
                ('title', models.CharField(max_length=140)),
                ('message', models.CharField(max_length=500)),
                ('message_url', models.URLField(blank=True)),
            ],
        ),
    ]