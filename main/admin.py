from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Bookings)
admin.site.register(Image)
admin.site.register(Plate)
admin.site.register(Comment)