from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import views, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been successfully created for {username}!')
            return redirect('blog:blog-main')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


class LoginView(views.LoginView):
    template_name = 'user/login.html'


def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html')