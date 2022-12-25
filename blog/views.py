
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def dashboard(request):
    return render(request, 'blog/dashboard.html')

def logout(request):
    return HttpResponseRedirect('/')

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                usname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user= authenticate(username=usname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'your login successfully!!!!!!!!!!!!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'your Registration successfully!!!!!!!!!!!')
            
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html',{'form':form})


