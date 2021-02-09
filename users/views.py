from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}!')
    #         return redirect('blog-home')
    else:
        form = UserRegistrationForm()
        # form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# messages.debug
# messages.success
# messages.info
# messages.error