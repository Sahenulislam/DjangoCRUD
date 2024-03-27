# views.py
from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import HttpResponseNotAllowed


def Student_Form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            if Student.objects.filter(student_id=student_id).exists():
                return HttpResponse('Student with this ID already exists.')
            else:
                student_name = form.cleaned_data['student_name']
                student_phone = form.cleaned_data['student_phone']
                form.save()
                return render(request, 'student_list.html', {'student_name': student_name, 'student_phone': student_phone})
    else:
        form = StudentForm()
    return render(request, 'StudentForm.html', {'form': form})



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def update_student(request, id):
    student = get_object_or_404(Student, student_id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  
            return redirect('student_list')  
    else:
        form =  StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})


def delete_student(request, id):
    if request.method == 'GET':
        # Retrieve all students with the specified ID
        students = Student.objects.filter(student_id=id)
        # Delete all retrieved students
        students.delete()
        return redirect('student_list')
    else:
        return HttpResponseNotAllowed(['GET'])


