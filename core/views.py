from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course, Grade
from .forms import StudentForm, StudentSearchForm, CourseForm, GradeForm


def home(request):
    return render(request, 'core/base.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

def student_update(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form})

def student_delete(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'core/student_confirm_delete.html', {'student': student})

def student_search(request):
    form = StudentSearchForm(request.GET)
    students = Student.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        age = form.cleaned_data.get('age')
        gender = form.cleaned_data.get('gender')

        if name:
            students = students.filter(name__icontains=name)
        if age:
            students = students.filter(age=age)
        if gender and gender != '':
            students = students.filter(gender=gender)

    return render(request, 'core/student_search.html', {'form': form, 'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'core/course_form.html', {'form': form})

def course_update(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'core/course_form.html', {'form': form})

def course_delete(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'core/course_confirm_delete.html', {'course': course})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'core/grade_list.html', {'grades': grades})

def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'core/grade_form.html', {'form': form})

def grade_update(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'core/grade_form.html', {'form': form})

def grade_delete(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'core/grade_confirm_delete.html', {'grade': grade})



