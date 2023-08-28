from typing import Any
from django.contrib.auth.decorators import login_required
from django .contrib import admin
from django.db.models import Q
from django.db.models.query import QuerySet
from .models import models
from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView,DeleteView,UpdateView,FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from dragons.models import Task
# Create your views here.

##def index(request):
  ##  return HttpResponse('HELLO every one')

class TaskList(ListView):
    model=Task
    context_object_name='tasks'

class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name='dragons/task.html'


class TaskCreate(LoginRequiredMixin,CreateView):
   model=Task
   fields='__all__'
   success_url=reverse_lazy('tasks')

class taskupdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')

class Search(ListView):
    model=Task
    context_object_name='tasks'
    template_name='dragons/task_list.html'

    def get_queryset(self):
        query=self.request.GET.get('serch-area')
        return Task.objects.filter(title__icontains=query)

class login(LoginView):
    template_name='dragons/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')   

class register(FormView):
     template_name='dragons/register.html'
     form_class=UserCreationForm
     redirect_authenticated_user=True
     success_url=reverse_lazy('tasks')

     def get (self,*args,**kwargs):
         if self.request.user.is_authenticated:
             return redirect ('tasks')
         return super(register,self).get(*args,**kwargs) 