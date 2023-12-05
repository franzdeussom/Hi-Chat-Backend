from django.contrib import admin

from publications.models import Publication, Comment

admin.site.empty_value_display = "--empty--"


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'body', 'media', 'background', 'public', 'kind', 'pub_date']
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'publication', 'owner', 'body', 'comment_date']
    date_hierarchy = 'comment_date'
    ordering = ['-comment_date']
