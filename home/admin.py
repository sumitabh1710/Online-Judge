from django.contrib import admin
from .models import problems, testcase, Verdict

# Register your models here.
admin.site.register(problems)
admin.site.register(testcase)
admin.site.register(Verdict)