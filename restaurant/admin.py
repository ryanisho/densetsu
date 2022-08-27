from django.contrib import admin
from .models import dimsumItems, appetizerItems, baoItems, noodleSoupItems, sushiItems, dessertItems, drinkItems, reservations, notification

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("title", "phone", "email", "time", "date", "people")

class dimSumAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class baoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class sushiAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class appetizerAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class dessertAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class drinkAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class noodleSoupAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "price")

class notificationAdmin(admin.ModelAdmin):
    list_display = ("title", "phone", "email", "message")

admin.site.register(dimsumItems, dimSumAdmin)
admin.site.register(appetizerItems, appetizerAdmin)
admin.site.register(baoItems, baoAdmin)
admin.site.register(noodleSoupItems, noodleSoupAdmin)
admin.site.register(sushiItems, sushiAdmin)
admin.site.register(dessertItems, dessertAdmin)
admin.site.register(drinkItems, drinkAdmin)
admin.site.register(reservations, ReservationAdmin)
admin.site.register(notification, notificationAdmin)
