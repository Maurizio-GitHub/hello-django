from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    # Firt test:
    def test_item_name_is_required(self):
        # It creates a form instance with an empty name field;
        # checks this field is not valid;
        # checks that there is a name-key in the dictionary of form.errors;
        # checks if the error message on name-key is 'This field is required.'
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    # Second test:
    def test_done_field_is_not_required(self):
        # It creates a form instance with a name field of 'Test Todo Items';
        # checks that this instance is valid, even without selecting 'done'.
        form = ItemForm({'name': 'Test Todo Items'})
        self.assertTrue(form.is_valid())

    # Third test (referring to what has been don into 'forms.py'):
    def test_fields_are_explicit_in_form_metaclass(self):
        # It creates an empty form instance;
        # checks that the Meta-fields are equal to 'name' and 'done'.
        # This also protects against the fields being reordered,
        # since the list must match exactly:
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
