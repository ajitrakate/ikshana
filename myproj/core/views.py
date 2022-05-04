from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import ImageForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import PhotoData
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
    return render(request, 'new/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'new/register.html', {'form': form})


def home(request):
    return render(request, 'new/home.html')

@login_required
def dashboard(request):
    images = PhotoData.objects.all().filter(userId=request.user.pk).order_by('time')[::-1]
    if len(images)>0:
        images = [images[0]]
    else:
        images = []
    # print(images)
    return render(request, 'new/Dashboard.html', {'user':request.user, 'images':images})

@login_required
def history(request):
    images = PhotoData.objects.all().filter(userId=request.user.pk).order_by('time')[::-1]
    # print(images)
    return render(request, 'new/history.html', {'user':request.user, 'images':images})


@csrf_exempt
def upload(request):  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form' : form})

# def upload2(request):  
#     if request.method == 'POST':
#         form = CustomForm(request.POST, request.FILES)
  
#         if form.is_valid():
#             time = form.cleaned_data['time']
#             userId = form.cleaned_data['userId']
#             print(time)
#             print(userId)
#             form.save()
#             return HttpResponse('Success')
#     else:
#         form = CustomForm()
#     return render(request, 'upload.html', {'form' : form})
