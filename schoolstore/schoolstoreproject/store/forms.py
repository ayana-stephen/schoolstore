from django import forms
from django.core.validators import RegexValidator
from .models import Student_Details,Department,Course


class Student_Form(forms.ModelForm):
    class Meta:
        model = Student_Details


        fields = ['name', 'dob', 'age', 'gender', 'phoneno', 'mailid', 'address', 'department', 'course', 'purpose',
                  'material']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['course'].queryset = Course.objects.none()