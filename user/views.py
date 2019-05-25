from django.contrib.auth.models import User
from django.shortcuts import render

from .forms import UserAddForm
from .models import Employee


def user_list(request):
    employees = Employee.objects.all().prefetch_related('user')

    return render(request, 'user/user_list.html', {'employees': employees})


def user_add(request):
    form = UserAddForm()
    context = {}

    if request.method == 'POST':
        form = UserAddForm(request.POST)

        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'],
                                       password=form.cleaned_data['password'])
            employee = Employee.objects.create(
                user=user, office=form.cleaned_data['office'])
            user.employee = employee
            user.save()

            context['success'] = True

    context['form'] = form

    return render(request, 'user/user_add.html', context)
