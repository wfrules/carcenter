from django.shortcuts import render
from django.http import HttpResponse
from carcenter.car import Car

gCar = Car()
 
def index(request):
    return render(request, "index.html", {})

def act(request):
    print(request.GET.get("dir"))
    return HttpResponse("act")
