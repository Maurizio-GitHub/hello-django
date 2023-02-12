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

# To install Heroku CLI in Gitpod:
# - curl https://cli-assets.heroku.com/install.sh | sh

# - use the login command: heroku login -i
# - enter your Heroku email
# - enter your Heroku API as password

# To view any other commands, just type: heroku

# If you need to know how any of these other commands work, just type:
# 'heroku' followed by the command and then the 'help' command. Example:
# heroku apps help
