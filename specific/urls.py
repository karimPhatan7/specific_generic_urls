from django.urls import *
from specific.views import *

app_name='specific'

urlpatterns=[
    path('hasen/',hasen,name='hasen'),
]