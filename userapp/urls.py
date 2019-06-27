from django.conf.urls import url
from userapp import views

app_name = 'userapp'

urlpatterns = [
    url('user-list', views.user_list_view, name='user_list'),
    url('user-form', views.user_form_view, name='user_form'),
]
