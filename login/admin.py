from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
  list_display = ('username', 'email', 'is_admin')
  search_fields = ('email',)


  list_filter = ()
  filter_horizontal = ()
  fieldsets = ()
  
admin.site.register(MyUser, MyUserAdmin)
