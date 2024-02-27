from django.db import models

# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.taskTitle}"
