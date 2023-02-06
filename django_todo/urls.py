"""
django_todo URL Configuration.

This file contains the routing information that allows users to type a specific
URL into their address bar and hit a specific Python function.
It is analogous to 'app.root' in Flask.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from todo.views import say_hello

# Once imported what we need, all that is left to do is define the url
# actually going to trigger our custom code and return the http response
# to the browser. To do that, we use the built-in path function,
# which typically takes three arguments:
# - the url that the user is going to type in;
# - the view function that it is going to return;
# - the name parameter:
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello, name='hello')
]
