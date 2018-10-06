from django.shortcuts import render, redirect

# import django UserCreation Form
from django.contrib.auth.forms import UserCreationForm

# import login as auth-login to prevent clasing with inbuilt,login view
from django.contrib.auth import login as auth_login

# import SignupForm from forms.py
from .forms import SignUpForm, EditProfileForm, UploadImageForm

from django.contrib.auth.decorators import login_required

from .models import Profile, Image


# Create your views here.


# PROFILE VIEW FUNCTION
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    profile = Profile.objects.get(user = request.user)
    image = Image.objects.all()
    return render(request, 'Profile/profile.html', {'profile': profile, 'image':image})


@login_required(login_url='/registration/login/')
def new_image(request):
    current_user = request.user

    if request.method == 'POST':
        upform = UploadImageForm(request.POST, request.FILES)
        if upform.is_valid():
            image = UploadImageForm.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')
    else:
        upform = UploadImageForm()
    return render(request, 'img.html', {"upform": upform})


@login_required(login_url='/registration/login/')
def profile_edit(request):
    """
    view function to render profile

    """
    form = EditProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()

            return redirect('profile')

    return render(request, 'Profile/profile_edit.html', {'form': form})


# SIGNUP VIEW FUNCTION
def signup(request):
    """
    signup form view function
    """
    # checking if request method is a post
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # form validationq
        if form.is_valid():
            # saving user credentials and creating uer instance  if form is valid
            user = form.save()

            # user passed as argument to auth_login function
            auth_login(request, user)
            return redirect('edit_profile')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration_form.html', {'form': form})

# def login(request):
#     """
#     login view function
#     :param request:
#     :return:
#     """
#     if request.method == 'POST':
#         form =
