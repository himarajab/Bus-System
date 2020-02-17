from django.contrib import admin

# Register your models here.
from .models import Driver,Bus

admin.site.register(Driver)
admin.site.register(Bus)