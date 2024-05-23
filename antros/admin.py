from django.contrib import admin
from .models import Antro, MenuItem, Review

@admin.register(Antro)
class AntroAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'approved', 'category', 'cost')
    list_filter = ('approved', 'category', 'cost')
    search_fields = ('name', 'contact', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'antro')
    list_filter = ('category', 'antro')
    search_fields = ('name', 'description', 'category')
    raw_id_fields = ('antro',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'antro')
    list_filter = ('rating', 'antro')
    search_fields = ('comment',)
    raw_id_fields = ('user', 'antro')