from django.urls import path
from lbus import views
urlpatterns=[
    path('routes',views.BusInfo,name='br')
]