from turtle import mode
from django.db import models

class login(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    date = models.DateField()

# Create your models here.
class problems(models.Model):
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'
    difficulty_level_choices = [(EASY, 'Easy'), (MEDIUM, 'Medium'), (HARD, 'Hard')]
    problem_name = models.CharField(max_length=200)
    problem_statement = models.TextField()
    difficulty_level = models.CharField(max_length=10, choices=difficulty_level_choices, default=EASY)
    #def __str__(self):
        #return self.problem_name

class testcase(models.Model):
    problem = models.ForeignKey(problems, on_delete=models.CASCADE)
    testcase = models.TextField()
    output = models.TextField()

class Verdict(models.Model):
    Success = "SUCCESS"
    COMPILATION_ERROR = "COMPILATION_ERROR"
    Wrong_Output = "Wrong Output"
    Time_Limit_Exceeded = "TIME LIMIT EXCEEDED"
    Runtime_Error = "RUNTIME ERROR"
    choices = [(Success, "SUCCESS"), (COMPILATION_ERROR, "COMPILATION_ERROR"), (Wrong_Output, "Wrong Output"), (Time_Limit_Exceeded, "TIME LIMIT EXCEEDED"), (Runtime_Error, "RUNTIME ERROR")]
    problem_01 = models.ForeignKey(problems, on_delete=models.CASCADE)
    verdict = models.CharField(
        max_length=20,
        choices=choices,
        default=Wrong_Output
    )
    submittedAt = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.problem_01.id + "_" + self.verdict



