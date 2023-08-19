from typing import Any
from django.db.models import Q
from django.db.models.query import QuerySet
from .models import models
from multiprocessing import context
from django.views.generic.list import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from dragons.models import Task
# Create your views here.

##def index(request):
  ##  return HttpResponse('HELLO every one')

class TaskList(ListView):
    model=Task
    context_object_name='tasks'
def search(self):
     search_input=self.request.Get.get('search-area') or ''
     if search_input:
      context['search_input']=search_input
     return context
class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name='dragons/task.html'

class TaskCreate(CreateView):
   model=Task
   fields='__all__'
   success_url=reverse_lazy('tasks')

class TaskDelete(DeleteView):
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

    


