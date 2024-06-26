from django.contrib import admin
from .models import Antro, MenuItem, Review

@admin.register(Antro)
class AntroAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'contact', 'approved', 'category', 'cost', 'location', 'image', 'description')
    list_filter = ('approved', 'category', 'cost', 'user')
    search_fields = ('name', 'contact', 'description', 'user__username', 'user__email')
    readonly_fields = ('location',)

    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'contact', 'approved', 'category', 'cost', 'location', 'image', 'description')
        }),
    )

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'antro', 'image', 'description')
    list_filter = ('category', 'antro')
    search_fields = ('name', 'description', 'category', 'antro__name')
    raw_id_fields = ('antro',)

    fieldsets = (
        (None, {
            'fields': ('antro', 'name', 'category', 'price', 'image', 'description')
        }),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'antro', 'comment')
    list_filter = ('rating', 'antro', 'user')
    search_fields = ('comment', 'user__username', 'user__email', 'antro__name')
    raw_id_fields = ('user', 'antro')

    fieldsets = (
        (None, {
            'fields': ('user', 'rating', 'antro', 'comment')
        }),
    )
