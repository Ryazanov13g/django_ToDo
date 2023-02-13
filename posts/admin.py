from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'actuality', 'user')
    fields = ('name', 'description', 'actuality', 'user', ('created_timestamp', 'updated_timestamp'))
    readonly_fields = ('created_timestamp', 'updated_timestamp')
    search_fields = ('name',)
    ordering = ('-actuality', '-created_timestamp')
