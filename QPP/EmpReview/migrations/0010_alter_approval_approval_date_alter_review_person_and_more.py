# Generated by Django 4.1.5 on 2023-03-03 22:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpReview', '0009_alter_employee_options_alter_approval_approval_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='approval_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 22, 8, 7, 31427, tzinfo=datetime.timezone.utc), help_text='Date of Approval'),
        ),
        migrations.AlterField(
            model_name='review',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EmpReview.person'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 3, 22, 8, 7, 31427, tzinfo=datetime.timezone.utc), help_text='Date of review'),
        ),
    ]
