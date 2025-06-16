from django.shortcuts import render
from django.views.generic import TemplateView

from apps.settings.models import Settings, ImageSlider, Bonus, Team

class IndexVIew(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings_id"] = Settings.objects.latest("id")
        context['image_all'] = ImageSlider.objects.all()
        context['bonus_all'] = Bonus.objects.all()
        context['team_all'] = Team.objects.all()
        return context
    