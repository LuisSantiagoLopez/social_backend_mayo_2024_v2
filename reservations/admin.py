from django.contrib import admin
from .models import Reservation, ReservationItem

class ReservationItemInline(admin.TabularInline):
    model = ReservationItem
    extra = 1

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'antro', 'user', 'cost', 'created_at']
    list_filter = ['antro', 'user', 'created_at']
    search_fields = ['user__username', 'antro__name']
    inlines = [ReservationItemInline]
