from django.shortcuts import render
from .models import Task

# Create your views here.
def TasksHome(request):

    data = {
        'mycounter': range(5),
        'mytasks': Task.objects.all()
    }

    mytasks = Task.objects.filter(title="Task 1")
    


    return render(request, 'tasks/index.html', data)
