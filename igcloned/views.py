from django.shortcuts import render, redirect

# import django UserCreation Form
from django.contrib.auth.forms import  UserCreationForm

# import login as auth-login to prevent clasing with inbuilt,login view
from django.contrib.auth import login as auth_login


# Create your views here.

# PROFILE VIEW FUNCTION
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
        form = UserCreationForm(request.POST)

        # form validation
        if form.is_valid():

            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form':form})

