from django.contrib import admin
from .models import Item

# Even though our tables have been created upon migration, and we could start
# creating items programmatically, we will not be able to see our items into
# admin until we expose them. To do that, we need to register our model here.

# Register your models here:
admin.site.register(Item)
