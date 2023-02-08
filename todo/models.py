from django.db import models

# When Django sees that we have created a new class, it will automatically
# create a related table when we make and run the database migrations.

# By themselves, our defined classes will do nothing. We need to use something
# called class inheritance to give them some functionality. Here, we inherit
# the base model class by putting models.model in the parentheses. In this way,
# our defined class can do everything the built-in Django model class can do.

# All that is left to do is define the attributes that our class will have.
# We can skip the 'id' field, since Django will create it for us automatically.


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # By default, all models that inherit this base model class will use its
    # built-in string method to display their class name, followed by the word
    # object. To change that, we need to override that string method with our
    # own, i.e. we need to redefine it here, in our own class. Therefore, it
    # is going to return the item class's name attribute, which is the name
    # that we put into the admin form online:
    def __str__(self):
        return self.name
