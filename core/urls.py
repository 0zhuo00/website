# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/new/', views.student_create, name='student_create'),
    path('students/<str:student_id>/edit/', views.student_update, name='student_update'),
    path('students/<str:student_id>/delete/', views.student_delete, name='student_delete'),
    path('students/search/', views.student_search, name='student_search'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/new/', views.course_create, name='course_create'),
    path('courses/<str:course_id>/edit/', views.course_update, name='course_update'),
    path('courses/<str:course_id>/delete/', views.course_delete, name='course_delete'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/new/', views.grade_create, name='grade_create'),
    path('grades/<int:grade_id>/edit/', views.grade_update, name='grade_update'),
    path('grades/<int:grade_id>/delete/', views.grade_delete, name='grade_delete'),
]