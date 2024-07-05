from django.contrib import admin
from taxi.models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number", )}),
    )
    add_fieldset = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number", )}),
    )

