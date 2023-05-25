from django.contrib import admin

from loogin.models import Followers

# Register your models here.
@admin.register(Followers)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("id",'full_name','email')
    search_fields = ("full_name","email")
    list_display_links = ("id","full_name")
    list_editable = ("email",)