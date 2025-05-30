from django.db import models
from django.core.validators import RegexValidator


class Student(models.Model):
    GENDER_CHOICES = [
    ('M', '男'),
    ('F', '女'),
    ]
    student_id = models.CharField(
        max_length=12,
        primary_key=True,
        validators=[RegexValidator(r'^\d{12}$','学号必须是12位数字')]
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    enrolled_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    
    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.score}"


