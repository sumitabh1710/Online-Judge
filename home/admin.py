from django.contrib import admin
from .models import login, problems, testcase

# Register your models here.
admin.site.register(problems)
admin.site.register(testcase)
admin.site.register(login)