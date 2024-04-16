from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('blog:blog-main')
        else:
            forms = UserRegisterForm()
    return render(request, 'user/register.html', {'forms': forms})
