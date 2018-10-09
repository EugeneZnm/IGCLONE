from django.shortcuts import render, redirect, get_object_or_404

# import django UserCreation Form
from django.contrib.auth.forms import UserCreationForm

# import login as auth-login to prevent clasing with inbuilt,login view
from django.contrib.auth import login as auth_login

# import SignupForm from forms.py
from .forms import SignUpForm, EditProfileForm, UploadImageForm, CommentForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Profile, Image, Follower, Comments


# Create your views here.


# PROFILE VIEW FUNCTION
@login_required(login_url='/registration/login/')
def profile(request):
    """
    view function to render profile

    """
    profile = Profile.objects.get(user = request.user)
    images = Image.objects.all()
    comments = Comments.objects.all()

    # getting followers instance
    # follower = Follower.objects.get(current_user=request.user)
    # followers = Follower.users.all()
    return render(request, 'Profile/profile.html', {'profile': profile, 'images':images, 'comments':comments, 'follower':follower})


@login_required(login_url='/registration/login/')
def new_image(request):
    current_user = request.user

    if request.method == 'POST':
        upform = UploadImageForm(request.POST, request.FILES)
        if upform.is_valid():

            new_image = upform.save( commit=False )
            new_image.user = current_user
            upform.save()
        return redirect('profile')
    else:
        upform = UploadImageForm()

    return render(request, 'Profile/img.html', {"upform": upform})


@login_required(login_url='/registration/login/')
def add_comment(request, image_id):

    images = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = images
            comment.save()
        return redirect('profile')


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


@login_required(login_url='/registration/login/')
def home(request):
    """
    render all users images
    :param request:
    :return:
    """
    images = Image.objects.all()
    comments = Comments.objects.all()

    return render(request, 'home.html', {'images': images, 'comments':comments})


@login_required(login_url='/registration/login/')
def follower(request, operation, pk):
    """
    view function to change followers

    """
    new_follower = User.objects.get(pk=pk)
    if operation == 'add':
        Follower.make_follower(request.user, new_follower)
    elif operation == 'remove':
        Follower.remove_follower(request, new_follower)

    return redirect('profile')


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
