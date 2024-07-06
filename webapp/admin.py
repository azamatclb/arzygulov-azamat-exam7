from django.contrib import admin

# Register your models here.

from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'date_added']
    list_display_links = ['id', 'author', 'email', 'date_added']
    list_filter = ['status', 'date_added', 'id', 'author']
    readonly_fields = ['date_added', 'date_updated']
    search_fields = ['id', 'author', 'email', 'date_added']


admin.site.register(GuestBook, GuestBookAdmin)
