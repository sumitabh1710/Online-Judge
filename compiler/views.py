from django.shortcuts import render
import sys
import subprocess

# Create your views here.
def compile_python(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        code1 = code.replace("\r\n", "<br />\r\n")
        try:
            sys.stdout = open('file.txt', 'w')
            exec(code)
            sys.stdout.close()
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            output = e
    return output

def compile_c(request):
    subprocess.run('g++ helloworld.cpp')
    output = subprocess.run('a.exe', capture_output=True, text=True)
    return output

def compile_java(request):
    pass