from django.contrib import admin
from .models import Customer,Cuisine,Chef,Food_Item,Event

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_id', 'contact_no') 
    #search_fields = ('name', 'email_id', 'contact_no')  
   # list_filter = ('favorite_cuisines',) 

admin.site.register(Customer, CustomerAdmin)  
admin.site.register(Cuisine)  
admin.site.register(Chef)
admin.site.register(Food_Item)
admin.site.register(Event)


# username: CMS
# password: cms1234