from django.contrib import admin
from BasicEntry import models
from BasicEntry.models import ComplaintType, District, Place, RequestType, SeekerTestQuestion
from BasicEntry.models import ShortTravelingPurpose, LongTravelingPurpose, PackageTravelingPurpose
from BasicEntry.models import VehicleType, VehicleModel, Weekday, DriveMode, DriveHour

# Register your models here.

admin.site.register(District)
admin.site.register(Place)
admin.site.register(ComplaintType)
admin.site.register(RequestType)
admin.site.register(SeekerTestQuestion)
admin.site.register(ShortTravelingPurpose)
admin.site.register(LongTravelingPurpose)
admin.site.register(PackageTravelingPurpose)
admin.site.register(VehicleType)
admin.site.register(VehicleModel)
admin.site.register(Weekday)
admin.site.register(DriveMode)
admin.site.register(DriveHour)

# class BasicEntryAdmin(admin.ModelAdmin):
#     ordering = ['id']
#     list_display_links= ['DistrictName']
#     list_display=['DistrictName']
#     list_filter=['DistrictName']
# admin.site.register(models.District, BasicEntryAdmin)
