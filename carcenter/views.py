from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")

def act(request):
    print(request)
    return HttpResponse("act")
