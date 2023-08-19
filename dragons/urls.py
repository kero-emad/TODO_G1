from django.urls import path
from .views import TaskCreate, TaskList,TaskDetail,TaskDelete,Search
from . import views

urlpatterns=[
  ##path('',views.index,name='index')
 path('',TaskList.as_view(),name='tasks'),
  path('create-task/',TaskCreate.as_view(),name='create-task'),
  path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
  path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
  path('Search/',Search.as_view(),name='Search'),
]