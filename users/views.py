from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registeruser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=UserRegisterForm()
		if request.method=='POST':
			form=UserRegisterForm(request.POST)
			if form.is_valid:
				form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, f'Account created for {username}!')
				return redirect('login')
		return render(request,'users/register.html',{'form':form})

def loginuser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')		
			password=request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'users/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('login')

def homepage(request):
    return render(request,'users/home.html')
