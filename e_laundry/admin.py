from django.contrib import admin
from e_laundry.models import demo
from e_laundry.models import Holder
from e_laundry.models import item
from e_laundry.models import orders

# Register your models here.

admin.site.register(demo)
admin.site.register(Holder)
admin.site.register(item)
admin.site.register(orders)