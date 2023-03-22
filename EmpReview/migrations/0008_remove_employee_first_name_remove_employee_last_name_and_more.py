# Generated by Django 4.1.5 on 2023-02-25 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreview', '0007_employee_first_name_employee_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='approval',
            name='approval_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 25, 2, 32, 53, 793711, tzinfo=datetime.timezone.utc), help_text='Date of Approval'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 25, 2, 32, 53, 793711, tzinfo=datetime.timezone.utc), help_text='Date of review'),
        ),
    ]
