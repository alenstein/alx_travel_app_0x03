from django.contrib import admin
from.models import Booking, Listing, Payment, Review

# Register your models here.
admin.site.register(Listing)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Booking)
