from django.contrib import admin

from .models import Category, Tour, TourImages


class TourImageInLine(admin.TabularInline):
    model = TourImages
    extra = 0


class AdminTour(admin.ModelAdmin):
    inlines = [TourImageInLine]


admin.site.register(Category)
admin.site.register(Tour)
admin.site.register(TourImages)
