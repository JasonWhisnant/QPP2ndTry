from django.contrib import admin
from .models import Person, Review, Approval, Employee
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.


class ReviewInline(admin.StackedInline):
    model = Review

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employees'
    fk_name = 'user'


# admin.site.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('employee',)

    inlines = [ReviewInline]

admin.site.register(Person, PersonAdmin)


# admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('person','ready_for_review')


admin.site.register(Review, ReviewAdmin)


# admin.site.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_filter = ('person','approved')
    model = Approval


admin.site.register(Approval, ApprovalAdmin)

class EmployeeAdmin(UserAdmin):
    inlines = (EmployeeInline,)
    list_display = ('username', 'email', 'managerId')
    search_fields = ['username','employee__userId', 'employee__managerId']

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(EmployeeAdmin, self).get_inline_instances(request, obj)

    def userId(self, obj):
        return Employee.objects.get(user=obj).userId

    def managerId(self, obj):
        return Employee.objects.get(user=obj).managerId


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
