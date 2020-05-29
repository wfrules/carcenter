from django.shortcuts import render
from django.http import HttpResponse
from carcenter.car import Car
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

gCar = Car()
 
def index(request):
    return render(request, "index.html", {})

def act(request):
    res = gCar.sendCmd(request.GET.get("dir"))
    return HttpResponse(res)

@csrf_exempt
def cmd(request):
    parms = request.POST.get('parms')
    parms = json.loads(parms)
    sCmd = parms['cmd']
    res = gCar.sendCmd(sCmd)
    objRet = json.loads(res)
    objRet['result'] = 0;
    return JsonResponse({'result':0, 'car': objRet})
