from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ["title", "description", "person_responsible"]
    success_url = reverse_lazy("tasklistowner")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "person_responsible"]

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasklistowner")
    

def Home(request):
    return render(request, 'task/home.html') 

class TaskListAssignee(LoginRequiredMixin, ListView):
    model = Task
    fields = ["title", "description", "person_responsible"]
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(person_responsible=user)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mode']='assignee'
        return context

class TaskListOwner(LoginRequiredMixin, ListView):
    model = Task
    fields = ["title", "description", "person_responsible"]
    paginate_by = 3
    # template_name = "task/task_listowner.html" 

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(created_by=user)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['mode']='owner'
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
   


