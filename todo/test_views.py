# Django imports the TestCase class. This class is an extension of the Python
# standard library module called 'unittest', which provides us with a bunch
# of methods to assert various things about our code:
from django.test import TestCase
from .models import Item


# Create your tests here:
class TestViews(TestCase):
    # Let's just remember that the following 'self' refers to 'TestDjango',
    # which, because it inherits the TestCase class, has a bunch of pre-built
    # methods and functionality that we can use.
    # First test:
    def test_get_todo_list(self):
        # It saves the homepage instance ('/') as response;
        # checks that the response code is 200;
        # checks that the template todo/todo_list.html is the same as response:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # Second test:
    def test_get_add_item_page(self):
        # Similar to test_get_todo_list:
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # Third test:
    def test_get_edit_item_page(self):
        # It creates an Item Object;
        # saves the response for that item;
        # asserts this item response code is 200;
        # asserts the template used is 'edit_item.html':
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # Fourth test:
    def test_can_add_item(self):
        # It creates a new item;
        # checks it redirects to the home page:
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    # Fifth test:
    def test_can_delete_item(self):
        # It creates a new item object instance;
        # deletes this item;
        # asserts that it redirects to the home page;
        # tries to return the item from the database using filter and item_id;
        # checks the length of existing_items = 0:
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    # Seventh test:
    def test_can_toggle_item(self):
        # It creates a new item object instance with done=True;
        # toggles this item so done=False;
        # asserts that it redirects to the home page;
        # gets the item again and saves it as updated_item;
        # checks the done status is False:
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
