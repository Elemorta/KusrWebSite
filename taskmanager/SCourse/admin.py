from django.contrib import admin
from .models import Town, Street, Bundle, Operator, Application


class BundleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name_Bundle', 'Count_channels', 'Count_films', 'Price', 'Date_begin', 'Date_end')
    search_fields = ('Date_begin', 'Price')


admin.site.register(Town)
admin.site.register(Street)
admin.site.register(Bundle, BundleAdmin)
admin.site.register(Operator)
admin.site.register(Application)