from django.contrib import admin
from .models import Services, WhyUs

#Editing the Data output in admin
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10





# Register your models here.
admin.site.register(Services, ServicesAdmin)
admin.site.register(WhyUs)