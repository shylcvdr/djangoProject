from django.contrib import admin
from django.contrib.admin import ModelAdmin

from treatment.models import Category, Treatment, Images


# Register your models here.



class TreatmentImageInline(admin.TabularInline):
    model=Images
    extra=5
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','category','price','amount']
    list_filter = ['status','category']

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'treatment','image','image_tag']
    Inlines = [TreatmentImageInline]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Treatment,TreatmentAdmin)
admin.site.register(Images,ImagesAdmin)