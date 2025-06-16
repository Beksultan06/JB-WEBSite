from django.contrib import admin
from apps.settings.models import Settings, ImageSlider, Bonus,Team
# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(ImageSlider)    
admin.site.register(Bonus)    
admin.site.register(Team)