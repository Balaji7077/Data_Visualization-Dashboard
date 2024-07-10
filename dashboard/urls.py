from django.urls import path
from dashboard.views import *

app_name='dash'

urlpatterns = [
     path('index', index, name='index'),
    path('DataListCreate/', DataListCreate.as_view(), name='DataListCreate'),
]
