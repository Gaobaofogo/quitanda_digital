from django.contrib.auth.models import Group, User

from .models import Employee


def createEmployee(form_data):
    user = User(username=form_data['username'])
    user.set_password(form_data['password'])
    user.save()

    employee = Employee.objects.create(user=user, office=form_data['office'])
    user.employee = employee
    user.save()

    giveAGroupToEmployee(user, form_data['office'])


def giveAGroupToEmployee(user, office):
    manager_group = Group.objects.get(name=office)
    user.groups.add(manager_group)
