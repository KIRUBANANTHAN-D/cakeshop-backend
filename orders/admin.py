from django.contrib import admin
from .models import Category, Cake, Branch ,Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'is_main', 'open_time', 'close_time')
    list_editable = ('is_main',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_no",
        "name",
        "phone",
        "cake",
        "weight",
        "egg_type",
        "delivery_type",
        "total",
        "status",
        "created_at",
    )
    search_fields = ("order_no", "name", "phone")
    list_filter = ("status", "created_at")