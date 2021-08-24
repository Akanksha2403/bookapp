from django.contrib import admin

from .models import Books, Orders, OrderUpdate, Contact

admin.site.register(Books)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Contact)