from django.contrib import admin
from .models import Department,Student_Details,Course

# Register your models here.
class Student_Details_Admin(admin.ModelAdmin):
   list_display = ['name']

admin.site.register(Student_Details,Student_Details_Admin)

class Department_Admin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Department,Department_Admin)

class course_Admin(admin.ModelAdmin):
   list_display = ['course_name']

admin.site.register(Course,course_Admin)