from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_posted', 'author']
    list_filter = ['title', 'date_posted']
    prepopulated_fields = { 'slug': ('title',)}

admin.site.register(Post, PostAdmin)
