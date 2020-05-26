from django.shortcuts import render
from django.http import HttpResponse
from carcenter.car import Car
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

gCar = Car()
 
def index(request):
    return render(request, "index.html", {})

def act(request):
    res = gCar.sendCmd(request.GET.get("dir"))
    return HttpResponse(res)

@csrf_exempt
def cmd(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})
