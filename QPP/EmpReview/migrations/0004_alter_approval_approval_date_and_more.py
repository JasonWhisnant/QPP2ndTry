# Generated by Django 4.1.5 on 2023-02-15 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpReview', '0003_alter_approval_approval_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='approval_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 55, 57, 484039, tzinfo=datetime.timezone.utc), help_text='Date of Approval'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 15, 17, 55, 57, 484039, tzinfo=datetime.timezone.utc), help_text='Date of review'),
        ),
    ]