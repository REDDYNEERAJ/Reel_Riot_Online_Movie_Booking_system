from django.contrib import admin
from .models import Movie, Theatre, Location, Show, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'runtime_minutes')
    filter_horizontal = ('locations',)

@admin.register(Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_list', 'total_seats')  # removed show_time
    filter_horizontal = ('locations', 'movies')

    # Custom method to show all locations in admin list_display
    def location_list(self, obj):
        return ", ".join([loc.name for loc in obj.locations.all()])
    location_list.short_description = 'Locations'

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theatre', 'show_time')
    list_filter = ('theatre', 'movie')
# ✅ NEW: Register Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'show', 'seat_number', 'booked_at')
    list_filter = ('show', 'user')
    search_fields = ('seat_number', 'user__username')