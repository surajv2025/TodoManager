from multiprocessing import context
from urllib import request

from django.shortcuts import render,redirect
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from todolist.forms import ContactForm
 
def homepage(request):
 
    
   return render(request,"todolist/homepage.html", {})

@login_required
def todolist(request): # jab user todolist per ayega to django todolist ko call karega aur info store karega user ke request ka
    if request.method=="POST": #Kya user ne form submit kiya hai?
        from_data=TaskForm(request.POST or None)#User ne jo data bheja hai, us data ko TaskForm ke andar daal do.
        if from_data.is_valid():
            
            instance = from_data.save(commit=False)#commit=False ka matlab hai ki abhi tak database mein save nahi karna hai, 
                                                  #sirf ek instance create karna hai
            instance.owner = request.user
            instance.save()
            messages.success(request,"Task Added Successfully")
            return redirect("todolist") # wapas kardo todolist per
        messages.success(request,"Task Not Added Successfully")
    
    all_tasks = Task.objects.filter(owner=request.user)#unhi tasks ko filter karo jinka owner current user hai
    paginator = Paginator(all_tasks, 8) # 8 tasks per page
    page=request.GET.get("page")
    
    all_tasks= paginator.get_page(page)
    context={
        'page':"Todo List",
        'all_tasks':all_tasks, ##Ab humein ye data HTML page ko dena hai.
    }
    
    return render(request,"todolist/todolist.html",context)#todolist.html page ko open karo aur uske andar context ka data bhejo.
@login_required
def delete_task(request,task_id):
    task_obj=Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.delete()
        messages.success(request,"Task Deleted Successfully")
    else:
        messages.error(request, "Access Denied")
    return redirect("todolist")
@login_required
def edit_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    
    if request.method == "POST":
        form_data = TaskForm(request.POST or None, instance=task_obj)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Task Updated Successfully")
            return redirect("todolist")
        else:
            messages.error(request, "Task Not Updated Successfully")
    
    # Context ko bahar rakh lo taaki GET request ya invalid POST dono me kaam kare
    context = {
        'task_obj': task_obj
    }
    
    # Yahan "edit_task.html" ki jagah "todolist/edit_task.html" karo
    return render(request, "todolist/edit_task.html", context)
@login_required
def complete_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = True
        task_obj.save()
        messages.success(request, "Task Marked as Completed Successfully")
    else:
        messages.error(request, "You are not the owner of this task.")
    return redirect("todolist")                                                                                                                              

def pending_task(request, task_id):
    task_obj = Task.objects.get(id=task_id)
    if task_obj.owner == request.user:
        task_obj.is_completed = False
        task_obj.save()
        messages.success(request, "Task Marked as Pending Successfully")
    else:
        messages.error(request, "You are not the owner of this task.")
    return redirect("todolist")                                                                                                                              


# Aapke baaki views yahan upar honge...

@login_required(login_url='login')  # Bina login ke contact page kholne par login page par bhej dega
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.user = request.user  # Logged-in user ki ID attach kar dega
            contact_instance.save()               # Database mein save ho jayega
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')            # Wapas contact page par redirect kar dega
    else:
        form = ContactForm()
    
    return render(request, 'todolist/contact.html', {'form': form})
   

def About(request):
    context={
        'page':"About Page"
    }
    return render(request,"todolist/About.html",context)