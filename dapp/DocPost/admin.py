from django.contrib import admin
from .models import DocPosts
# Register your models here.


@admin.register(DocPosts)
class DocPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    list_filter = ('is_published', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('date',)