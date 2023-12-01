from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title =  models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user_creator', null=True)
    person_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_responsible')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
	    return reverse('taskdetail', kwargs={'pk':self.pk})
    



