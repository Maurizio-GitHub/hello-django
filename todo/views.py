# All files in this folder have been created by entering
# 'python3 manage.py startapp todo' command into Terminal.

# As we need access to our models, we need to import them:
from django.shortcuts import render, redirect
from .models import Item

# Django projects are organized into small components called apps.
# We can think of an app as a reusable self-contained collection of
# code that can be passed around from project to project in order to
# speed up development time.

# Create your views here:


# The first thing that we obviously need to do is render a web page. Let's
# define a function that we can make available to the browser through
# 'urls.py'. There, we import this function:
def get_todo_list(request):
    # Here, we import all the items into the view and pass it into the
    # template inside the context object:
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # If the request is a post-request, it means it came from someone
    # clicking the submit button on our form. Therefore, we want to
    # actually create a to-do item and then redirect back to the home
    # page to show the user their updated to-do lists:
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')

    return render(request, 'todo/add_item.html')
