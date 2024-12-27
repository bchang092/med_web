from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to user-specific home page
            if user.is_superuser:
                return redirect('admin_home')
            else:
                return redirect('user_home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_home(request):
    return render(request, 'accounts/user_home.html')

@login_required
def admin_home(request):
    return render(request, 'accounts/admin_home.html')
