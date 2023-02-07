# All files in this folder have been created by entering
# 'python3 manage.py startapp todo' command into Terminal.
from django.shortcuts import render

# Django projects are organized into small components called apps.
# We can think of an app as a reusable self-contained collection of
# code that can be passed around from project to project in order to
# speed up development time.


# The first thing that we obviously need to do is render a web page. Let's
# define a function that we can make available to the browser through
# 'urls.py'. There, we import this function:
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')

# Create your views here.
