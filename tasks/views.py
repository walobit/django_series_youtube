from django.shortcuts import render

# Create your views here.
def TasksHome(request):
    return render(request, 'tasks/index.html')
