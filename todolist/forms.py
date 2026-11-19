from django import forms
from todolist.models import ContactMessage, Task 
class TaskForm(forms.ModelForm): # ready made model form main se ak new form create karo jisaka name TaskForm h
    class Meta: # class Meta main hum model ka name or fields ka name define karte h
        model = Task
        fields = ['task',"is_completed"]
        
# Naya Contact Form yahan niche add karein
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message']       