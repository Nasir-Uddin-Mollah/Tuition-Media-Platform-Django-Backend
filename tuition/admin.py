from django.contrib import admin
from . import models
# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Class, ClassAdmin)


class TuitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'subjuct', 'class_name', 'is_available']
    search_fields = ['title', 'subjuct', 'class_name']
    list_per_page = 10


admin.site.register(models.Tuition, TuitionAdmin)
