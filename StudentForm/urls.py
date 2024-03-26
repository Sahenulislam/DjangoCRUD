# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.Student_Form, name='student_form'),
    path('read/', views.student_list, name='student_list'),
    path('update/<str:id>/', views.update_student, name='update_student'),

]
