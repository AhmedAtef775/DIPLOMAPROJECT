from django.contrib import admin
from .models import Course, Question, Result, Option


admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Option)
