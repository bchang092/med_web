from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from reviews.models import volunteer

#Home page
def home_page (request):
    #render home page
    return render(request, 'authentication/home.html') 

#Login/Registration Page: 
def register_login(request):
    #Register/login page that has option to go to Register or login
    return render(request, 'authentication/login_register.html') 

#User Registration
def register_user(request):
    #post a dictionary like object that can temporarily handle data sent via HTTP
    if request.method == 'POST':
        username = request.POST['username']
        vol_fname = request.POST['vol_fname']
        vol_lname = request.POST['vol_lname']
        email = request.POST['email']
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            storage = messages.get_messages(request)
            return render(request, 'authentication/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already taken!")
            storage = messages.get_messages(request)
            return render(request, 'authentication/register.html')
        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1,
                                            first_name=vol_fname, last_name=vol_lname )
            user.save()

            login_url = reverse('login')
            return redirect(login_url)
        except:
            storage = messages.get_messages(request)
            messages.error(request, "Username already exists!")
    #sanity check; shouldn't reach this line of code
    storage = messages.get_messages(request)
    return render(request, 'authentication/register.html')


# User Login View
def login_user(request):
    storage = messages.get_messages(request)

    #check passcode
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user - Django internal controls 
        user = authenticate(request, username=username, password=password) #returns none if nothing is found
        if user is not None:
            login(request, user)
            # messages.success(request, "Logged in successfully!")
            volunteer_url = reverse('volunteer_page')  # Named URL for the volunteer page
            return redirect(volunteer_url)

        else:
            messages.error(request, "Invalid username or password! Try again.")

    #clear out messages after they are redered once
    return render(request, 'authentication/login.html')


#need to implement this logout function on the user interface
# User Logout View
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

