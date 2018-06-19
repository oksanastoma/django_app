from django.contrib import admin
from editor.models import Contact


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
