from django.urls import re_path
from AppTwo import views

urlpatterns=[
    re_path(r'^help/$',views.help,name='help'),
]