from django.shortcuts import render
from django.views.generic import TemplateView

from apps.settings.models import Settings, ImageSlider, Bonus, Team, About, Services
from apps.settings.search import SearchMixin

class IndexVIew(TemplateView, SearchMixin):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings_id"] = Settings.objects.latest("id")
        context['image_all'] = ImageSlider.objects.all()
        context['bonus_all'] = Bonus.objects.all()
        context['team_all'] = Team.objects.all()
        return context
    

class AboutView(TemplateView, SearchMixin):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings_id"] = Settings.objects.latest("id")
        context['image_all'] = ImageSlider.objects.all()
        context['about_id'] = About.objects.latest("id")
        return context

class PortfolioView(TemplateView, SearchMixin):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings_id"] = Settings.objects.latest("id")
        context['about_id'] = About.objects.latest("id")
        return context

class ServicesView(TemplateView, SearchMixin):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["settings_id"] = Settings.objects.latest("id")
        context['image_all'] = ImageSlider.objects.all()
        context['about_id'] = About.objects.latest("id")
        context['services_all'] = Services.objects.all()  
        context['services_id'] = Services.objects.latest("id") 
        return context