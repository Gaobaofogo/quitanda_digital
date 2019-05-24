from django.urls import include, path

from .views import user_list

app_name = 'user'

urlpatterns = [path('', user_list, name='user_list')]
