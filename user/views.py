from django.shortcuts import render


def user_list(request):
    return render(request, 'user/user_list.html')


def user_add(request):
    return render(request, 'user/user_add.html')
