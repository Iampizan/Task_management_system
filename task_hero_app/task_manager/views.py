from django.shortcuts import render, redirect

def home(request):
    return render(request, 'task/home_page.html')
def task_details(request):
    return render(request, 'task/task_details.html')
