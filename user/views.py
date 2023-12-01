from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import RegisterForm

class Login(auth_views.LoginView):
    template_name = 'user/login.html'
    redirect_field_name = ''

class Logout(auth_views.LogoutView):
    template_name = 'user/logout.html'

def Register(request):  
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f" account for {username} created successfully")
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('login'))
        

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, "user/register.html", {"form": form})

