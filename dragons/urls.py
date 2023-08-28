from django.urls import path
from .views import TaskCreate, TaskList,TaskDetail,TaskDelete,taskupdate,Search,login,register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
  ##path('',views.index,name='index')
 path('',TaskList.as_view(),name='tasks'),
  path('create-task/',TaskCreate.as_view(),name='create-task'),
  path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
  path('update-task/<int:pk>/',taskupdate.as_view(),name='update-task'),
  path('delete-task/<int:pk>/',TaskDelete.as_view(),name='delete-task'),
  path('Search/',Search.as_view(),name='Search'),
  path('login/',login.as_view(),name='login'),
  path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
  path('register/',register.as_view(),name='register'),
]