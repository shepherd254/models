from django.shortcuts import render
from modelapp.form import StudentForm


def home(request):
    mimi = StudentForm
    return render(request, 'index.html', {'form':mimi})
