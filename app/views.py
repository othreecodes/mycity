from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'app/index.djt')


def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        number = request.POST.get("number")




    return render(request, 'app/register.djt')
