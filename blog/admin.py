from django.contrib import admin
from .models import Post, PostCategory
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    search_fields = ['title', 'author', 'category', 'status']
    list_display = (
        'title',
        'author',
        'category',
        'status',
        'last_updated',
    )


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)