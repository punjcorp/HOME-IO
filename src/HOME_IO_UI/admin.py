from django.contrib import admin

# Register your models here.
from .models import IOSwitch, IOSwitchGroup, IOSwitchActivity

admin.site.register(IOSwitch)
admin.site.register(IOSwitchGroup)
admin.site.register(IOSwitchActivity)
