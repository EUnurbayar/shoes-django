from django.contrib import admin
from .models import Shoes
from .models import Brand

# Register your models here.
admin.site.register(Shoes)
admin.site.register(Brand)