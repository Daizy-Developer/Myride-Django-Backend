from django.contrib import admin
from dashboard.models import Driver, User,Promo_Code, All_Ride_Historie,Ride_offer,Driver_offer,User_Message,Driver_Message,Saved_Destination,Earning
admin.site.register(User)
admin.site.register(All_Ride_Historie)
admin.site.register(Promo_Code)
admin.site.register(Ride_offer)
# admin.site.register(Ride_Details)
admin.site.register(Driver_offer)
admin.site.register(User_Message)
admin.site.register(Driver_Message)
admin.site.register(Saved_Destination)

class Earning_Inline(admin.TabularInline):
    model = Earning
    raw_id_fields = ['driver']
# admin.site.register(nameFile)

@admin.register(Driver)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['UId','name','date_of_birth','gender','phone_number','driver_image','vehicle_no','vehicle_name','license_no','insurance_no','ratings','last_location_lat','last_location_long','current_location_lat','current_location_long']
    # list_filter = ['paid', 'created', 'updated']
    inlines = [Earning_Inline]


    