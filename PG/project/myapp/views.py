from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout as log, login as auth_login
import requests


# Create your views here.

def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        u = User.objects.create_user(username, email, password)
        u.save()
        return redirect('/')
    else:
        return render(request, 'sign-up.html')
     #    return redirect('')
     #    # return HttpResponse(
     #    #     "Registration complete! Please head over to the <a href='/login/'>login page</a> to start using your website.")
     #    else :
     #
     # return render(request, 'sign-up.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_authenticated:
                auth_login(request, user)
                return render(request, 'index.html')
            else:
                return redirect('signin')
        else:
            messages.add_message(request, messages.INFO, 'Username/Password is wrong...!')
            return redirect('signin')
    else:
            return render(request, 'sign-in.html')



@login_required(login_url='/signin')
def logout(request):
    log(request)
    return redirect('/')

@login_required(login_url='/signin')
def property(request):
    return render(request,'property.html')

@login_required(login_url='/signin')
def agents(request):
    return render(request,'about-us.html')

@login_required(login_url='/signin')
def news(request):
    return render(request, 'blog.html')

@login_required(login_url='/signin')
def pages(request):
    return render(request, 'property-details.html')

@login_required(login_url='/signin')
def contact(request):
    return render(request, 'contact.html')
