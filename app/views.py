from .models import Profile

from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect


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
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        u = User()

        u.first_name = fname
        u.last_name = lname
        u.username = uname
        u.email = email

        u.set_password(password)
        u.save()

        p = Profile()
        p.user = u
        p.address = address
        p.phone_number = number
        p.save()

        return redirect('app:index')

    return render(request, 'app/register.djt')
