from django.shortcuts import render
from .models import Student, Coaches

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def student_list(request):
    if request.method == 'POST':
        form = Student(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Student()

    return render(request, 'main/student_list.html' , {
        'students': Student.objects.all()
    })

def coaches_list(request):
    return render(request, 'main/coaches_list.html' , {
        'coaches': Coaches.objects.all()
    })