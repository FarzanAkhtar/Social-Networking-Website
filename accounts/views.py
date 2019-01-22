from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model,login , logout
from .forms import UserLoginForm, UserRegisterationForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile



@login_required
def home(request):
    name = UserProfile.objects.all()
    return render(request,'accounts/home.html',{'name': name})

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect('accounts:home')

    return render(request, "accounts/login.html" ,{'form':form})


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterationForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=username, password=password)
        login(request,new_user)

        if next:
            return redirect(next)
        return redirect('accounts:home')

    return render(request,'accounts/signup.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def profile_view(request):
    name = get_object_or_404(UserProfile, pk=request.POST.get('user'))
    return render(request, 'accounts/profile.html', {'name': name})






@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:home')

    else:
        form = ProfileEditForm(instance=request.user)
        return render(request,'accounts/profile_edit.html', {'form': form})




def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile-view')

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'accounts/change_password.html',{'form': form})



