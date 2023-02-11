# In Django, it is possible to create forms directly from the model itself,
# and allow Django to handle all the form validations. We just need to create
# a new file - this one - in our app directory.
from django import forms
from .models import Item


# The idea of creating this form in Django is that rather than writing an
# entire form ourselves in HTML, we can simply render it out as a template
# variable. To make sure it is available for use in the HTML template, we
# need to import this item-form into views.py.
# Just like when we created the item-model itself, our form will be a class
# that inherits a built-in Django class to give it some basic functionality:
class ItemForm(forms.ModelForm):
    #  The Meta inner-class gives our form some information about itself,
    # such as which fields to render or how to display errors: it tells the
    # form which model it is going to be associated with (the fields: 'name'
    # and 'done' have already been defined in models.py):
    class Meta:
        # These are the fields to explicitly display in the inner Meta-class.
        # The reason for that is, otherwise, the form will display all fields
        # on the model, including those we might not want the user to see:
        model = Item
        fields = ['name', 'done']
