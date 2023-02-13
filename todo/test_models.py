from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    # It creates a new item instance and checks that item.done is False:
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    # # It creates a new item instance and checks it equals to the string
    # returned by the __str__ method (i.e. self.name):
    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')


# Finally, to know how much of our code we have actually tested, we can do
# this with a useful tool called coverage:

# In the Terminal:
# - pip3 install coverage (to install the tool);
# - coverage run --source=todo manage.py test (to run it);
# - coverage report (to check report results);
# - coverage html (to create a folder containing interactive HTML report);
# - python3 -m http.server (to view the index.html file produced).
