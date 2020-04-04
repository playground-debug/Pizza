from django.contrib import admin
from .models import Regular_Pizza, Sicilian_Pizza, Topping, Sub, Dinner_Platter, Pasta, Salad, Order, Placed_Order, AddOn

# Register your models here.
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_Platter)
admin.site.register(Order)
admin.site.register(Placed_Order)
admin.site.register(AddOn)
