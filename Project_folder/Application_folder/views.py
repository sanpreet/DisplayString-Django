# Create your views here.
from django.http import HttpResponse
#here is the response to the request and this function is passed in the urls.py file so that this response is
#shown in the web at http://127.0.0.1:8000/
def index(request):
    return HttpResponse("My name is Sanpreet Singh. Django is the web framework for perfectionists with deadlines:")

