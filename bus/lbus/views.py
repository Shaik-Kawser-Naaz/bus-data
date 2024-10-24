from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def BusInfo(request):
    d={'routes':[
    {'id':'bus1','area':'dharmavaram'},
    {'id':'bus2','area':'atp'},
    {'id':'bus3','area':'tadipathri'},
    {'id':'bus4','area':'pamidi'},
    {'id':'bus5','area':'bks'}
    ]}
    return render(request,'info.html',d)