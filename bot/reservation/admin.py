from django.contrib import admin
from .models import Person, PersonStatus, Role

# Register your models here.

admin.site.register(Person)
admin.site.register(PersonStatus)
admin.site.register(Role)
