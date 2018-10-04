from django.shortcuts import render

# import django UserCreation Form
from django.contrib.auth.forms import  UserCreationForm


# Create your views here.


# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form':form})

