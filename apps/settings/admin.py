from django.contrib import admin
from apps.settings.models import Settings, ImageSlider, Bonus,Team, About, Services
from modeltranslation.admin import TranslationAdmin

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ['id', 'title']

admin.site.register(ImageSlider)    
admin.site.register(Bonus)    
admin.site.register(Team)
admin.site.register(About)
admin.site.register(Services)