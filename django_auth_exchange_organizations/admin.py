from django.contrib import admin
from . import models


class DomainOrganizationAdmin(admin.ModelAdmin):
    list_filter = ()
    list_display = ('domain', 'organization')
    search_fields = list_display
    readonly_fields = ('created', 'updated')


admin.site.register(models.DomainOrganization, DomainOrganizationAdmin)
