from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.task_list, name='task_list'),

    path('', lambda request: HttpResponseRedirect('/tasks/')),
]