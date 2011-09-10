from django.contrib import admin
from profiles.models import UserProfile, Gender

class GenderAdmin(admin.ModelAdmin):
  pass

class UserProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(Gender, GenderAdmin)
admin.site.register(UserProfile, UserProfileAdmin)