from django.contrib.admin.options import ModelAdmin
from .models import Plan, ThumbnailSize, Image, UserPlan

from django.contrib.admin import site

class PlanAdmin(ModelAdmin):
    list_display = ('pk', 'plan_name', 'acces_original', 'expiration_links')
        
class ThumbnailSizeAdmin(ModelAdmin):
    list_display = ('pk', 'h', 'w', 'plan')

class UserPlanAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'plan')

class ImageAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'image', 'thumbnail200', 'thumbnail400')

site.register(Plan, PlanAdmin)
site.register(ThumbnailSize, ThumbnailSizeAdmin)
site.register(UserPlan, UserPlanAdmin)
site.register(Image, ImageAdmin)
