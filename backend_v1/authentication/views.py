from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
#validating email imports;
from validate_email_address import validate_email
from django.core.validators import validate_email as django_validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser
from .forms import UserRegisterForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

#Home page
def home_page (request):
    #render home page
    return render(request, 'authentication/home.html') 

#Login/Registration Page: 
def register_login(request):
    #Register/login page that has option to go to Register or login
    return render(request, 'authentication/login_register.html') 


def signup_view(request):
    if request.method == "POST":
        next = request.GET.get('next')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            else:
                return redirect('verify-email')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/register.html', context)

#sending email item
User = get_user_model()
def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('authentication/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'authentication/verify_email.html')

def verify_email_done(request):
    return render(request, 'authentication/verify_email_done.html')

#verifying link user clicks on 
def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'authentication/verify_email_confirm.html')

#verify that email verification process is complete:
def verify_email_complete(request):
    return render(request, 'authentication/verify_email_complete.html')



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

