from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, UserAddForm
from .models import Employee
from .utils import createUserAndGivesHimAGroup


@login_required
@permission_required('user.view_employee')
def user_list(request):
    employees = Employee.objects.all().prefetch_related('user')

    return render(request, 'user/user_list.html', {'employees': employees})


@login_required
@permission_required('user.add_employee')
def user_add(request):
    form = UserAddForm()
    context = {}

    if request.method == 'POST':
        form = UserAddForm(request.POST)

        if form.is_valid():
            createUserAndGivesHimAGroup(form)
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
                next = request.GET.get('next', '')

                if next:
                    return redirect(next)

                return redirect(reverse('home'))
            else:
                context['user_not_exist'] = True

    context['login_form'] = login_form

    return render(request, 'user/login.html', context)


def logout(request):
    auth_logout(request)

    return redirect(reverse('login'))
