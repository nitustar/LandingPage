from django.shortcuts import render
# from django.http import HttpResponse
from mysite.models import Student

# Create your views here.

def index(request):
    print(request.method)
    if request.method == 'POST' :
        fname = request.POST.get('fname')
        email = request.POST.get('email')

        s = Student(firstname=fname, email=email)
        s.save()
    return render(request, 'mysite/index.html')
