# Generated by Django 4.1.5 on 2023-02-24 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('EmpReview', '0005_alter_approval_approval_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={},
        ),
        migrations.RemoveField(
            model_name='person',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mgr_first_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='mgr_last_name',
        ),
        migrations.AddField(
            model_name='person',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='EmpReview.employee'),
        ),
        migrations.AddField(
            model_name='person',
            name='mgr_name',
            field=models.ForeignKey(default=0, help_text='Manager Name', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Manager_Name', to='EmpReview.employee'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='approval_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 17, 56, 34, 279366, tzinfo=datetime.timezone.utc), help_text='Date of Approval'),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 17, 56, 34, 279366, tzinfo=datetime.timezone.utc), help_text='Date of review'),
        ),
    ]
