from django.contrib import admin
from .models import Category, Package,Booking,PackageImage

admin.site.register(Category)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(PackageImage)