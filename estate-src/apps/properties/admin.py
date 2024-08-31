from django.contrib import admin
from .models import Property,PropertyViews

class PropertAdmin(admin.ModelAdmin):
    list_display = ["title","country","advert_type","property_type"]
    list_filter = ["advert_type","property_type","country"]


admin.site.register(Property,PropertAdmin)
admin.site.register(PropertyViews)
