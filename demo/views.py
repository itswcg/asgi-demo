from django.http import HttpResponse


# Create your views here.

def http_index(request):
    return HttpResponse("Hello, world")
