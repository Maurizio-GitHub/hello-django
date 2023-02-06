# All files in this folder have been created by entering
# 'python3 manage.py startapp todo' command into Terminal.
from django.shortcuts import render, HttpResponse


# The first thing that we obviously need to do is render some sort of web page.
# Just to demonstrate how this works, let's define a simple python function
# called 'say_hello'.
# All this python function is going to do is take an http-request from the user
# and return an http-response to the user that says 'Hello!'.

# We can make this function available to the web browser through 'urls.py'.
# There, we import this function:
def say_hello(request):
    return HttpResponse('Hello!')

# Django projects are organized into small components called apps.
# We can think of an app as a reusable self-contained collection of
# code that can be passed around from project to project in order to
# speed up development time.

# Create your views here.
