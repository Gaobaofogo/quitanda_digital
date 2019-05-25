from django.contrib.auth.models import Group, User

from .models import Employee


def createUserAndGivesHimAGroup(form):
    user = User(username=form.cleaned_data['username'])
    user.set_password(form.cleaned_data['password'])
    user.save()

    employee = Employee.objects.create(user=user,
                                       office=form.cleaned_data['office'])
    user.employee = employee
    user.save()

    manager_group = Group.objects.get(name=form.cleaned_data['office'])
    user.groups.add(manager_group)
