"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ #The client doesn't directly access our files but has to go through this
    path('', views.home, name="Home"),
    path('admin/', admin.site.urls), #'Pattern to watch for in typed URL', 'function to call to build that particular webpage'
    path('', include('products.urls')), #Tells Django to add the contents module products.urls in the list of urls to watch for
]
urlpatterns += staticfiles_urlpatterns()
