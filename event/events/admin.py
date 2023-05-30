from django.contrib import admin

from .models import Organization, Event


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'address', 'postcode')
    search_fields = ('title', 'description', 'address', 'postcode')
    list_filter = ('postcode', )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'image_icon',
        'date',
        'get_organizations'
    )
    search_fields = ('title', 'description', 'date')
    list_filter = ('date', )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Event, EventAdmin)
