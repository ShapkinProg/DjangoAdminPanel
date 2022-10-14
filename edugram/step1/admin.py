from django.contrib import admin
from .models import *


class vuzAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count_views', 'count_guests', 'VK_Subs', 'VK_Video', 'YT_Subs', 'YT_Views', 'TG_Subs')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'wiki', 'vk', 'vk_subs')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


admin.site.register(vuz, vuzAdmin)
admin.site.register(Person, PersonAdmin)
