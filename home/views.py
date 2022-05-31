from multiprocessing import context
from django.contrib import messages
from re import template
from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import problems, Verdict
from compiler.views import compile_c, compile_python
from django.contrib.auth.models import User, auth

def home(request):
    questions = problems.objects.all()
    return render(request, 'home.html', {'questions': questions})

def contact(request):
    return render(request, 'contact.html')

def problem(request, variable_id):
    question = problems.objects.get(id=variable_id)
    type_comp = ['None', 'Python', 'C++', 'Java']
    context = {
        'var0': question.id,
        'var1': question.problem_statement,
        'var2': type_comp
    }
    return render(request, 'problem.html', context)

def submit(request, variable_id):
    if request.POST['type'] == 'Python':
        output = compile_python(request, variable_id)
    if request.POST['type'] == 'C++':
        output = compile_c(request, variable_id)
    if request.POST['type'] == 'Java':
        output = compile_java(request, variable_id)
    recent_submissions = Verdict.objects.all().order_by('-submittedAt')[:10]
    context = {
        'output' : output,
        "result": recent_submissions
    }
    return render(request, 'leaderboard.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password= password1)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('register')
        return redirect('home')
    else:    
        return render(request, 'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

