from django.contrib import admin
from .models import Product , UserProfile

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    pass
class UserAdmin(admin.ModelAdmin) :
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(UserProfile , UserAdmin)

