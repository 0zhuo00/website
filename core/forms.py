from django import forms
from .models import Student, Course, Grade


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'gender', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'name', 'description', 'start_date', 'end_date']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'score']

class StudentSearchForm(forms.Form):
    name = forms.CharField(required=False, label='学生姓名')
    age = forms.IntegerField(required=False, label='学生年龄')
    gender = forms.ChoiceField(required=False, label='学生性别', choices=[('', '全部'), ('M', '男'), ('F', '女')])

