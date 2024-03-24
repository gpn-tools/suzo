from django.contrib import admin

# Register your models here.

from .models import Staff, Position_titles, Org_elements
admin.site.register(Staff)
admin.site.register(Position_titles)
admin.site.register(Org_elements)

