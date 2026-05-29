from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating')
    list_filter = ('rating', 'product')
