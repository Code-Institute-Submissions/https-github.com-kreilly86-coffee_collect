from django.contrib import admin
from .models import Coffee


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('producer', 'slug', 'region',)
    search_fields = ['producer', 'flavournotes']
    list_filter = ('producer', 'region', 'variety', 'process')
    prepopulated_fields = {'slug': ('producer',)}
