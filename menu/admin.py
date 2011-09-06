from django.contrib import admin
from menu.models import Menu, MenuItem

class MenuAdmin(admin.ModelAdmin):
  pass

class MenuItemAdmin(admin.ModelAdmin):
  pass

admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)