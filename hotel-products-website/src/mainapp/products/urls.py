from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ #url path, command to carry out, shortcut
    path('admin_console', views.admin_console, name="admin"), #"name" is the shorcut we can use to call on this url command
    path('<int:pk>/details/', views.details, name="details"), #pk is passed into views.details
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirmdelete/', views.confirmed, name="confirm"),
    path('createRecord/', views.createRecord, name="createRecord"),
]