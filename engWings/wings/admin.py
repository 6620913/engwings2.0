from django.contrib import admin

# Register your models here.

from .models import Videos,Courses
admin.site.register(Videos)

admin.site.register(Courses)