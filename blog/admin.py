from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'publish_date', 'status')
    list_filter = ('status', 'writer', 'publish_date')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    raw_id_fields = ('writer',)
    prepopulated_fields = {'slug': ('title',)}
