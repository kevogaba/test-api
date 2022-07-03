from django.contrib import admin
from api.models import Accomplishment, Indicator, Measurement

admin.site.register(Accomplishment)
admin.site.register(Indicator)
admin.site.register(Measurement)