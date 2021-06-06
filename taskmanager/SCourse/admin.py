from django.contrib import admin
from .models import Town, Street, Bundle, Operator, Application

admin.site.register(Town)
admin.site.register(Street)
admin.site.register(Bundle)
admin.site.register(Operator)
admin.site.register(Application)