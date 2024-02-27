from django import forms 
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta :
        model = TaskModel
        exclude = ["completed",'id']
        labels = {
            "taskTitle" : "Title",
            "taskDescription" : "Description",
        }
        help_texts = {
            "taskTitle" : "Title of your Work",
            "taskDescription" : "Description of your Work",
        }