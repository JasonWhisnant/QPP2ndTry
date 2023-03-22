# Generated by Django 4.1.5 on 2023-02-24 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreview', '0006_alter_person_options_remove_person_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='approval',
            name='approval_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 22, 58, 35, 896443, tzinfo=datetime.timezone.utc), help_text='Date of Approval'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 22, 58, 35, 896443, tzinfo=datetime.timezone.utc), help_text='Date of review'),
        ),
    ]
