from django.contrib import admin
from .models import Todo
admin.site.site_header="Todo Admin"
admin.site.site_title="Todo Admin Area"
admin.site.index_title="Welcome to Todo admin area"

admin.site.register(Todo)