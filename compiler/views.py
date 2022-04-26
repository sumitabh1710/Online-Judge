from django.shortcuts import render
import sys
import subprocess
from datetime import datetime
from home.models import problems, testcase, Verdict

# Create your views here.
def compile_python(request, variable_id):
    tests = testcase.objects.filter(problem__id = variable_id)
    code = request.POST['code']
    for test in tests:
        input = test.testcase
        expected = test.output
        try:
            file = open('temp.py', 'w')
            file.write(code)
            file.close()
            output = subprocess.run([sys.executable, 'temp.py'], capture_output=True, encoding='ascii', input=input, timeout=1)
            actual = output.stdout
            if (output.returncode != 0):
                verdict = Verdict.COMPILATION_ERROR
            elif actual == expected:
                verdict = Verdict.Success
            elif subprocess.TimeoutExpired:
                verdict = Verdict.Time_Limit_Exceeded
            else:
                verdict = Verdict.Wrong_Output
        except Exception as e:
            verdict = Verdict.Runtime_Error
    sol = Verdict(
        problem_01 = problems.objects.get(pk = variable_id),
        verdict = verdict,
        submittedAt = datetime.now
    )
    sol.save()
    return verdict

def compile_c(request, variable_id):
    code = request.POST['code']
    try:
        file = open('temp.cpp', 'w')
        file.write(code)
        file.close()
        subprocess.run('g++ temp.cpp')
        output = subprocess.run('a.exe', capture_output=True, text=True)
        #output = subprocess.run([sys.executable, 'temp.cpp'], capture_output=True, text=True)
        output = output.stdout
    except Exception as e:
        output = e
    return output

def compile_java(request, variable_id):
    pass