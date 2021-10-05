from django.contrib import admin
from .models import Post,Tag,Category

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'published_date', 'visible')
  list_filter = ('tags__slug', 'author__username')
  search_fields = ['title',]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
