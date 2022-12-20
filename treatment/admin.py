from django.contrib import admin

from treatment.models import Category, Treatment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','category','price','amount']
    list_filter = ['status','category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Treatment,TreatmentAdmin)