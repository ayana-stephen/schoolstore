from django.db import models


# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='student_department'
        verbose_name_plural='student_departments'
    def __str__(self):
        return '{}'.format(self.name)
class Course(models.Model):
    course_name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    course_desc=models.TextField(blank=True)
    class Meta:
        ordering=('course_name',)
        verbose_name='student_course'
        verbose_name_plural='student_course'
    def __str__(self):
        return '{}'.format(self.course_name)
class Student_Details(models.Model):
    name=models.CharField(max_length=250,unique=True)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phoneno=models.IntegerField()
    mailid=models.EmailField()
    address=models.CharField(max_length=250)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose=models.CharField(max_length=250)
    material=models.CharField(max_length=250)
    class Meta:
        ordering=('name',)
        verbose_name='student_details'
        verbose_name_plural='student_details'
    def __str__(self):
        return '{}'.format(self.name)






