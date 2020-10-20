from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'reply_to', 'username', 'email', 'home_page')
    # list_display_links = ('text',)
