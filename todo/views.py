# All files in this folder have been created by entering
# 'python3 manage.py startapp todo' command into Terminal.

# As we need access to our models, we need to import them:
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

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

        # NEW WAY:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

        # OLD WAY:
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
        # return redirect('get_todo_list')

    # With the ItemForm imported, we can create an instance of it here
    # and return the context containing it to the template:
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # We can get a copy of the item from the database by using a built-in
    # django shortcut ('get_object_or_404'), which we will use to say we
    # want to get an instance of the item model with an id equal to the
    # item id that was passed into the view via the URL:
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # To pre-populate the form with the item's current details, we can pass
    # an instance argument to the form, prefilled with the information for
    # the item we have just got from the database:
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


# This function/view will not have a template because it is just going to
# toggle the item status and then redirect back to the to-do list:
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


# No-template scenario applies to this function (only a URL is needed):
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
