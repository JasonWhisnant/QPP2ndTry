import uuid

from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views import generic
from .models import Person, Review, Approval, Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from okta.client import Client as OktaClient
import asyncio
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ReviewForm, ApprovalForm, PersonForm, EmpSearch
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.models import User
from django.db import IntegrityError
from dal import autocomplete

# View for Autocomplete

class NameAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        #if not self.request.user.is_authenticated:
            #return Employee.objects.none()
        qs = Employee.objects.all()

        if self.q:
            qs = qs.filter(user__first_name__istartswith=self.q)

        return qs
@login_required
def index(request):
    review_approval_needed = Review.objects.filter(approver__user__username=request.user).filter(ready_for_review=True).count()
    review_update_needed = Review.objects.filter(reviewer__user__username=request.user).filter(ready_for_review=False).count()

    context = {
        'review_approval_needed': review_approval_needed,
        'review_update_needed': review_update_needed,
    }

    return render(request, 'index.html', context=context)

@login_required
def search_person(request):

    all_users = {}
    results = {}

    # print(currentUsers)
    if 'name' in request.GET:
        name = request.GET['name'].capitalize()

        all_users = Employee.objects.all().filter(user__first_name=name) | Employee.objects.all().filter(user__last_name=name)
    return render(request, 'empreview/people_choice.html', {"all_users": all_users})

def get_or_create(request, id):

    person, created = Person.objects.get_or_create(employee=Employee.objects.get(id=id))

    return redirect('person-update', pk=person.pk)




class PersonView(LoginRequiredMixin, generic.ListView):
    model = Person
    paginate_by = 10
    context_object_name = 'people_list'
    redirect_field_name = 'people'


# class PersonDetailView(LoginRequiredMixin, generic.DetailView):
    # model = Person

def PersonDetail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404("Person does not exist. Person Detail View")
    form = ReviewForm()
    return render(request, 'empreview/person_detail.html', context={'person':person, 'form':form})


class PersonUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Person
    fields = (
            'mgr_name',
            'current_position',
            'new_position',
            'current_path',
            'new_path',
            'current_job',
            'new_job',
            'current_level',
            'new_level',
        )


class ReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = Review



class ApprovalDetailView(LoginRequiredMixin, generic.DetailView):
    model = Approval


class ReviewsByRequester(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = 'empreview/my_created_reviews.html'
    paginate_by = 10

    def get_queryset(self):
        return Review.objects.filter(reviewer__user__username=self.request.user).order_by('review_date')


class ReviewsByApprover(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = 'empreview/reviews_approval.html'
    paginate_by = 10

    def get_queryset(self):
        return Review.objects.filter(approver__user__username=self.request.user).order_by('review_date')


from .models import Person, Review
from django.utils.translation import gettext_lazy as _


"""class PersonCreate(CreateView):
    model = Person
    fields = ['employee', 'mgr_name', 'current_position', 'new_position', 'current_path', 'new_path', 'current_job',
              'new_job', 'current_level', 'new_level']
"""
def add_person(request):

    if request.method == "POST":
        form = PersonForm(request.POST)
        person = Person()
        if form.is_valid():
            employee = form.cleaned_data['employee']
            current_position = form.cleaned_data['current_position']
            new_position = form.cleaned_data['new_position']
            current_path = form.cleaned_data['current_path']
            new_path = form.cleaned_data['new_path']
            current_job = form.cleaned_data['current_job']
            new_job = form.cleaned_data['new_job']
            current_level = form.cleaned_data['current_level']
            new_level = form.cleaned_data['new_level']

            person.employee = employee
            person.mgr_name = request.user.employee
            person.current_position = current_position
            person.new_position = new_position
            person.current_path = current_path
            person.new_path = new_path
            person.current_job = current_job
            person.new_job = new_job
            person.current_level = current_level
            person.new_level = new_level
            person.save()

        return redirect('person-detail', pk=person.id)

    else:

        form = PersonForm()

    return render(request, 'empreview/person_form.html', {"form": form, "user": request.user})


class PersonUpdate(UpdateView):
    model = Person
    fields = ['employee', 'mgr_name', 'current_position', 'new_position', 'current_path', 'new_path', 'current_job',
              'new_job', 'current_level', 'new_level']


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('people')


##########################
# Review CRUD Operations #
##########################

@login_required
def add_review(request, pk=None):

    try:
        person_instance = Person.objects.get(pk=pk)
    except Person.objects.get(pk=pk).DoesNotExist:
        raise Http404("Error in review post")


    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            approver = form.cleaned_data['approver']
            role_info = form.cleaned_data['role_info']
            person_info = form.cleaned_data['person_info']
            performance_quality = form.cleaned_data['performance_quality']
            performance_goals = form.cleaned_data['performance_goals']
            skills_require = form.cleaned_data['skills_require']
            skills_compare = form.cleaned_data['skills_compare']
            values_company = form.cleaned_data['values_company']
            values_interest = form.cleaned_data['values_interest']
            communication_appropriate = form.cleaned_data['communication_appropriate']
            communication_respect = form.cleaned_data['communication_respect']
            leadership_principles = form.cleaned_data['leadership_principles']
            leadership_motivate = form.cleaned_data['leadership_motivate']
            feedback = form.cleaned_data['feedback']

            review = Review()
            review.person = person_instance
            review.reviewer = form.cleaned_data['reviewer']
            review.approver = approver
            review.role_info = role_info
            review.person_info = person_info
            review.performance_quality = performance_quality
            review.performance_goals = performance_goals
            review.skills_require = skills_require
            review.skills_compare = skills_compare
            review.values_company = values_company
            review.values_interest = values_interest
            review.communication_appropriate = communication_appropriate
            review.communication_respect = communication_respect
            review.leadership_principles = leadership_principles
            review.leadership_motivate = leadership_motivate
            review.feedback = feedback
            review.review_date = datetime.now()
            review.ready_for_review = True
            review.save()

            return render(request, 'success.html', context={'stype':'review'})

        else:
            person_mgr = get_object_or_404(Employee, userId=person_instance.employee.managerId)
            form = ReviewForm(initial={"reviewer": person_mgr})

    return render(request, reverse('person-detail', kwargs={'pk': person_instance.id}), {'person': person_instance.id,
                                                                                        'form': form})


@login_required
class ReviewUpdate(UpdateView):
    model = Review
    fields = '__all__'
@login_required
class ReviewDelete(DeleteView):
    pass

@login_required
def add_approval(request, pk):
    try:
        review_instance = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        approval_instance = Approval.objects.get(pk=pk)


    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            approval_date = form.cleaned_data['approval_date']
            business_case = form.cleaned_data['business_case']
            base_salary = form.cleaned_data['base_salary']
            currency_type = form.cleaned_data['currency_type']
            variable_comp = form.cleaned_data['variable_comp']
            budget = form.cleaned_data['budget']
            equity = form.cleaned_data['equity']
            next_increase = form.cleaned_data['next_increase']

            approval = Approval()
            approval.person = review_instance.person
            approval.review = review_instance
            approval.approval_date = approval_date
            approval.business_case = business_case
            approval.base_salary = base_salary
            approval.currency_type = currency_type
            approval.variable_comp = variable_comp
            approval.budget = budget
            approval.equity = equity
            approval.next_increase = next_increase
            approval.final_approver = review_instance.approver
            approval.approved = True

            approval.save()
            review_instance.ready_for_review = False

            return render(request, 'success.html', context={'stype': 'approval'})
    else:
        form = ApprovalForm()

    return render(request, 'empreview/approval_form.html', {'object': review_instance, 'form': form, 'id':id})


def success(request, stype):
    return render(request, 'success.html', {'stype': stype})

#################
# Okta DB files #
#################

from .get_all_okta_users import get_all_users as oktausers

"""
def add_users_to_db(request):
    all_users = {}
    # currentEmps = set(Person.objects.values_list('first_name', 'last_name', flat=False))

    # print(currentUsers)



    config = {
        'domain': 'eso',
        'token': '00wRZl_kpU3eHwWjQgfb1TtuGzec52ddOIE4-p_FHB',
        'param': 'filter=status eq "ACTIVE"'
    }
    
    okta_client = OktaClient(config)
    paras = {'filter': 'status eq "ACTIVE"', 'limit': 1000}

    async def main(parameters):
        users, resp, err = await okta_client.list_users()
        return users

    users = asyncio.run(main(paras))
    
    errors = []
    success = []
    

    users = oktausers(config['domain'],config['token'],config['param'])

    for user in users:
        try:
            new_user = User.objects.create_user(user['profile']['email'],
                                                user['profile']['email'],
                                                user['profile']['firstName']+"Pass")
            new_user.first_name = user['profile']['firstName']
            new_user.last_name = user['profile']['lastName']
            success.append((new_user.email, new_user.first_name, new_user.last_name))
            new_user.save()

        except IntegrityError:
            errors.append(user)
        except AttributeError:
            errors.append(user)



    return render(request, 'success.html', {"all_users": all_users, "errors": errors, "success":success})

def create_or_update_profile(request):
    # creates and updates profiles by pulling userId and managerId from Okta
    noID = []
    not_in_okta = []
    added = []
    config = {
        'orgUrl': 'https://eso.okta.com',
        'token': '00wRZl_kpU3eHwWjQgfb1TtuGzec52ddOIE4-p_FHB'
    }
    okta_client = OktaClient(config)

    for emp in Employee.objects.all():
        emp.userId = ''
        emp.managerId = ''
        emp.first_name = ''
        emp.last_name = ''

        async def main(user):
            user, resp, err = await okta_client.get_user(user)
            return user

        p_user = asyncio.run(main(emp.user.username))

        if p_user:
            try:
                emp.userId = p_user.id
                emp.managerId = p_user.profile.managerId
                emp.user.first_name = p_user.profile.firstName
                emp.user.last_name = p_user.profile.lastName
                emp.save()
                added.append((emp, p_user.profile.firstName, emp.user.first_name, p_user.profile.lastName, emp.user.last_name))
            except IntegrityError:
                not_in_okta.append((emp, emp.userId, emp.managerId))
        else:
            not_in_okta.append(emp)

        if emp.userId == '' and emp.managerId == '':
            emp.delete()
            noID.append(emp)

    return render(request, 'success.html', {'noID': noID, 'not_in_okta': not_in_okta, "added": added})
"""

def scratch_test(request):
    data = Employee.objects.all().filter(user__first_name__istartswith='L')
    emps = data

    return render(request, 'empreview/scratchtest.html', {'emps': emps})