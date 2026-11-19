from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import customRegistrationForm
def register(request):
    if request.method == 'POST':
       register_form = customRegistrationForm(request.POST)    
       if register_form.is_valid():
           register_form.save()
           messages.success(request, 'Account created successfully')
           return redirect('todolist')
    else:
         register_form = customRegistrationForm()
    return render(request, 'register.html', {'register_form': register_form})
# Create your views here.
