from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the challenges index.")

def january(request):
    return HttpResponse("Hello, world. You're at the January challenge.")

def february(request):
    return HttpResponse("Hello, world. You're at the February challenge.")