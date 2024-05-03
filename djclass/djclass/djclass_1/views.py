from django.shortcuts import render,redirect
from .models import Post
from .models import PythonModel
from .models import webCCC
from .models import webgo
from .models import webjavascript
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
from .forms import LoginForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def python_list(request):
    python_objects = PythonModel.objects.all()
    return render(request, 'python.html', {'python_objects': python_objects})

def web_cc(request):
    webb_ccc = webCCC.objects.all()
    return render(request,'C++.html', {'webb_ccc':webb_ccc})

def webgo_app(request):
    webgo_objects  =  webgo.objects.all()
    return render(request, 'go.html', {'webgo_objects': webgo_objects})

def web_java_script(request):
    web_javascript =  webjavascript.objects.all()
    return render(request,'javascript.html',{'web_javascript':web_javascript})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправление на домашнюю страницу после успешного входа
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})