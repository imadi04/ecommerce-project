from django.contrib import admin
from cart.models import UserProfileInfo,Product,Order,OrderUpdate
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderUpdate)
