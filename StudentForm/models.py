# models.py
from django.db import models

class Student(models.Model):
    student_id=models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)  
    student_phone = models.CharField(max_length=20)  
