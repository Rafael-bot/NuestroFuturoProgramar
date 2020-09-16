from django.contrib import admin

# Register your models here.
from Cerveza.models import cerveza,compañia,specialIngridients


# Cerveza
class CervezaAdmin(admin.ModelAdmin):
    list_display = ('name','abv','is_filtered')
    list_filter = ('is_filtered',)
    exclude = ('created_by','last_modified_by')

admin.site.register(cerveza,CervezaAdmin)
admin.site.register(compañia)
admin.site.register(specialIngridients)




