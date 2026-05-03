from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "You have successfully created an account")
            form.save()
            return redirect("users:login")
        print("Form has errors: ")
        print(form.errors)
        
    context = {"form": form}
    return render(request, "users/register.html", context)