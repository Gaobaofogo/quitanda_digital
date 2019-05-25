from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, UserAddForm
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
            user = User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()

            employee = Employee.objects.create(
                user=user, office=form.cleaned_data['office'])
            user.employee = employee
            user.save()

            context['success'] = True

    context['form'] = form

    return render(request, 'user/user_add.html', context)


def login(request):
    login_form = LoginForm()
    context = {}

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(request,
                                username=request.POST['username'],
                                password=request.POST['password'])

            if user is not None:
                auth_login(request, user)

                return redirect(reverse('home'))
            else:
                context['user_not_exist'] = True

    context['login_form'] = login_form

    return render(request, 'user/login.html', context)
