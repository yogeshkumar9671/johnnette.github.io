from django.contrib import admin
from new_app.models import AddressModel, Country, State, District, City, StudentAddress

# Register your models here.

admin.site.register(AddressModel)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(City)
admin.site.register(StudentAddress)
