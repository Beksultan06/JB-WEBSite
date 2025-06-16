from modeltranslation.translator import register, TranslationOptions
from .models import Settings, Bonus, Team, About, Services

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'title', 'description',
        'title2', 'description2',
        'title_bonus1', 'title_bonus2', 'title_team'
    )

@register(Bonus)
class BonusTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'role',)

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text',)

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'title_obj',)
