from django.contrib import admin

from home.models import Setting, ContactFormMessage

# Register your models here.
admin.site.register(Setting)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','emai','subject','status']
    list_filter = ['status']
admin.site.register(ContactFormMessage,ContactFormAdmin)