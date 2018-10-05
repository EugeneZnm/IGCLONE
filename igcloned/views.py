from django.shortcuts import render, redirect

# import django UserCreation Form
from django.contrib.auth.forms import  UserCreationForm

# import login as auth-login to prevent clasing with inbuilt,login view
from django.contrib.auth import login as auth_login

# import SignupForm from forms.py
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required

# Create your views here.


# PROFILE VIEW FUNCTION
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    return render(request, 'Profile/profile.html')



# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validation
        if form.is_valid():

            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration_form.html', {'form':form})


# def login(request):
#     """
#     login view function
#     :param request:
#     :return:
#     """
#     if request.method == 'POST':
#         form =