from django.shortcuts import render

# Create your views here.
def TasksHome(request):
    data = {
        'mycounter': range(5),
        'name': 'leondaz',
        'longword': 'this channel is leondaz'
    }
    return render(request, 'tasks/index.html', data)
