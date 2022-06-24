from django.contrib.auth import authenticate
from django.contrib.auth import login as loginUser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import calc

# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request ,'index.html')

def login(request):
    if request.method=='GET':
        form= AuthenticationForm()
        context={
            "form":form
        }
        return render(request ,'login.html',context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('index')

        else:
            context={
            "form":form
            }
            return render(request ,'login.html',context=context)


def signup(request):
    if request.method == 'GET':
        form= UserCreationForm()
        context={
            'form':form
        }
        return render(request ,'signup.html',context=context)
    else:
        print(request.POST)
        form= UserCreationForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            user= form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request ,'signup.html',context=context)

@login_required(login_url='login')
def history(request):
    user = request.user
    data = calc.objects.filter(user = user).all()
    print(data)
    return render(request, 'history.html', context={'calc': data, 'user': user})

def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def calci(request):
    res = ''
    num1 = ''
    num2 = ''
    operator = ''
    if request.method == 'POST':
        num1 = int(request.POST.get('number1'))
        user = request.user
        num2 = int(request.POST.get('number2'))
        operator = request.POST.get('operator')
     
        if operator == '+':
            res = num1 + num2
        if operator == '-':
            res = num1 - num2
        if operator ==  '*':
            res = num1 * num2
        if operator ==  '/':
            res = num1 / num2
        if operator ==  '^':
            res = num1 ** num2
        if operator ==  '%':
            res = num1 % num2

        
        calc.objects.create(operand1 = num1, operand2 = num2 ,operation = operator , result = res, user = user)
           
    return render(request,'index.html', context={'res': res, 'num1':num1, 'num2':num2, 'operator':operator})