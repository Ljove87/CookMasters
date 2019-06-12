from django.contrib import admin
from .models import Post

from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_ckeditor.widgets import CKEditorWidget


class PostForm(ModelForm):
    class Meta:
        widgets = {
            'name': CKEditorWidget(editor_options={'startupFocus': True})
        }


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ['title', 'slug', 'date_posted', 'author']
    list_filter = ['title', 'date_posted']

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
