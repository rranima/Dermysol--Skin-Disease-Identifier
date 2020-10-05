from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


import keras.models
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
import scipy.misc
import json

CATEGORIES = ["Acne-Rosacea", "Basal cell carcinoma",
             " Herpes"," Melanoma Skin Cancer Nevi and Moles","Urticaria Hives"," Vasculitis"," Warts"]

model = load_model('./models/DERMYSOLv2skin_net_frz10_100ep.hdf5')
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

# Create your views here.
def registeruser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            try:
                if form.is_valid:
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Account created for {username}!')
                    return redirect('login')
            except ValueError:
                messages.info(request, '')
        return render(request, 'users/register.html', {'form': form})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'users/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('home')


def homepage(request):
    return render(request, 'users/home.html')


def dashboard(request):
    return render(request, 'users/dashboard.html')


def predictimage(request):
    if request.method == 'POST':
        fileobj = request.FILES['filepath']
        fs = FileSystemStorage()
        filePathName=fs.save(fileobj.name,fileobj)
        filePathName = fs.url(filePathName)
        testimage = '.'+filePathName
        img = image.load_img(testimage, target_size=(150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        images = np.vstack([x])
        classes = model.predict(images)
        maximum = 0.9
        for i, value in enumerate(classes[0]):
            if value > maximum:
                index = i
        prediction = CATEGORIES[index]
        context = {'filePathName':filePathName,'prediction':prediction}
        return render(request, 'users/upload.html', context)
    else:
        return render(request, 'users/upload.html')
      
