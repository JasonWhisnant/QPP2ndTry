import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone as tz
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userId = models.CharField(max_length=50, blank=True)
    managerId = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50)

    def name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        ordering = ('user__last_name', 'user__first_name')


class Person(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='employee', null=True)
    manager_Name = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None,
                                     related_name="Manager_Name", null=True)

    current_position = models.CharField(max_length=100)
    new_position = models.CharField(max_length=100)

    PATHS = (
        ('m', 'Management -- this is any position that involves managing people'),
        ('e', 'Expert -- this is any position that does not involve managing people'),
    )

    current_path = models.CharField(
        max_length=1,
        choices=PATHS,
        blank=True,
        default='e',
    )
    new_Career_Path = models.CharField(
        max_length=1,
        choices=PATHS,
        blank=True,
        default='e',
        help_text="(choose even if the path is not changing)"
    )

    JOBS = (
        ('x', 'Executive'),
        ('m', 'Management'),
        ('s', 'Sales'),
        ('t', 'Technical'),
        ('p', 'Professional'),
        ('c', 'Client Services'),
    )

    current_Job_Category = models.CharField(
        max_length=1,
        choices=JOBS,
        blank=True,
    )

    new_Job_Category = models.CharField(
        max_length=1,
        choices=JOBS,
        blank=True,
        help_text="(choose even if the category is not changing)"
    )

    LEVELS = (
        ('e7', 'E7'),
        ('m6', 'M6'),
        ('m5', 'M5'),
        ('m4', 'M4'),
        ('m3', 'M3'),
        ('m2', 'M2'),
        ('sm5', 'SM5'),
        ('sm3', 'SM3'),
        ('s5', 'S5'),
        ('s4', 'S4'),
        ('s3', 'S3'),
        ('s2', 'S2'),
        ('s1', 'S1'),
        ('t5', 'T5'),
        ('t4', 'T4'),
        ('t3', 'T3'),
        ('t2', 'T2'),
        ('t1', 'T1'),
        ('p5', 'P5'),
        ('p4', 'P4'),
        ('p3', 'P3'),
        ('p2', 'P2'),
        ('p1', 'P1'),
        ('cm5', 'CSM5'),
        ('cm2', 'CSM2'),
        ('cs5', 'CS5'),
        ('cs4', 'CS4'),
        ('cs3', 'CS3'),
        ('cs2', 'CS2'),
    )

    current_level = models.CharField(
        max_length=3,
        choices=LEVELS,
        blank=True,
        help_text="Current Level")

    new_level = models.CharField(
        max_length=3,
        choices=LEVELS,
        blank=True,
        help_text="New Level")

    requester = models.CharField(
        max_length=1,
        blank=True,
        help_text="Not Used")

    class Meta:
        # ordering = ['last_name', 'first_name']
        app_label = 'EmpReview'

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.employee.user.last_name}, {self.employee.user.first_name}'


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular review")
    person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True)
    review_date = models.DateField(default=tz.now, help_text="Date of review")
    reviewer = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True, related_name='reviewer',
                                 help_text="Manager writing the review")
    approver = models.ForeignKey(Employee, max_length=50,
                                 on_delete=models.DO_NOTHING, related_name='appover',
                                 help_text="Manager who will be approving")
    role_info = models.TextField(max_length=1000, help_text="Role information (please see text on the page for more"
                                                            "information).")
    person_info = models.TextField(max_length=1000, help_text="Info about the person (please see text on the page"
                                                              "for more information).")
    performance_quality = models.BooleanField(blank=True, help_text="Work Quality")
    performance_goals = models.BooleanField(blank=True, help_text="Meeting Goals")
    skills_require = models.BooleanField(blank=True, help_text="Required skills")
    skills_compare = models.BooleanField(blank=True, help_text="Skills compared to colleagues")
    values_company = models.BooleanField(blank=True, help_text="Company Values")
    values_interest = models.BooleanField(blank=True, help_text="Interest in projects")
    communication_appropriate = models.BooleanField(blank=True, help_text="Communicate appropriately?")
    communication_respect = models.BooleanField(blank=True, help_text="Communicate with respect?")
    leadership_principles = models.BooleanField(blank=True, help_text="Show leadership principles?")
    leadership_motivate = models.BooleanField(blank=True, help_text="Motivate Others?")
    feedback = models.TextField(max_length=1000, help_text="Specific feedback from others")
    ready_for_review = models.BooleanField(blank=True, default=True, help_text="Ready for manager approval")

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.person.employee.user.last_name}; {self.review_date}'

    def meta(self):
        app_label = 'EmpReview'


class Approval(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this approval")
    review = models.OneToOneField('Review', on_delete=models.DO_NOTHING, null=True)
    person = models.ForeignKey('Person', on_delete=models.DO_NOTHING, null=True)
    approval_date = models.DateField(default=tz.now, help_text="Date of Approval")
    business_case = models.BooleanField(blank=True, help_text="Meets business requirements?")
    base_salary = models.DecimalField(max_digits=7, decimal_places=2, help_text="New Salary")

    CURRENCY = (
        ('gbp', 'British Pound'),
        ('cad', 'Canadian Dollars'),
        ('usd', 'US Dollars'),
    )

    currency_type = models.CharField(max_length=3, choices=CURRENCY, help_text="Currency Type")

    variable_comp = models.CharField(max_length=200, help_text="Variable Compensation Element?")
    budget = models.BooleanField(blank=True, help_text="Budget available?")
    equity = models.BooleanField(blank=True, help_text="Trigger Equity or LTIP?")
    next_increase = models.BooleanField(blank=True, help_text="Exclude from next increase?")
    final_approver = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, help_text="Final Approver")
    approved = models.BooleanField(blank=True, help_text="Approved?")

    def get_absolute_url(self):
        return reverse('approval-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.person.employee.name}, {self.review.review_date}'


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
        print("Profile created for", User)


@receiver(post_save, sender=User)
def save_employee_profile(sender, instance, **kwargs):
    instance.employee.save()
    print("Profile saved")
