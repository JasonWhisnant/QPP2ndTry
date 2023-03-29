from django.forms import ModelForm, ModelChoiceField, TextInput, Select
from EmpReview.models import Person, Review, Approval, Employee
from django.utils.translation import gettext_lazy as _


class EmpSearch(ModelForm):

    class Meta:
        model = Person
        fields = ('employee',)
        widgets = {'employee': Select(attrs={'class': 'form-control'})}

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = (
            'employee',
            'current_position',
            'new_position',
            'current_path',
            'new_path',
            'current_job',
            'new_job',
            'current_level',
            'new_level',
        )

        widgets = {
            'employee': Select(attrs={'class': 'form-control'}),
            'current_position': TextInput(attrs={'class': 'form-control'}),
            'new_position': TextInput(attrs={'class': 'form-control'}),
            'current_path': Select(attrs={'class': 'form-control'}),
            'new_path': Select(attrs={'class': 'form-control'}),
            'current_job': Select(attrs={'class': 'form-control'}),
            'new_job': Select(attrs={'class': 'form-control'}),
            'current_level': Select(attrs={'class': 'form-control'}),
            'new_level': Select(attrs={'class': 'form-control'}),
        }


class PersonEditForm(ModelForm):
    class Meta:
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

        widgets = {
            'current_position': TextInput(attrs={'class': 'form-control'}),
            'new_position': TextInput(attrs={'class': 'form-control'}),
            'current_path': Select(attrs={'class': 'form-control'}),
            'new_path': Select(attrs={'class': 'form-control'}),
            'current_job': Select(attrs={'class': 'form-control'}),
            'new_job': Select(attrs={'class': 'form-control'}),
            'current_level': Select(attrs={'class': 'form-control'}),
            'new_level': Select(attrs={'class': 'form-control'}),
        }


# Create Review Form
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['id', 'person', 'review_date', 'ready_for_review']


# Approval Form
class ApprovalForm(ModelForm):
    class Meta:
        model = Approval
        exclude = ['id', 'review', 'final_approver', 'approved']
