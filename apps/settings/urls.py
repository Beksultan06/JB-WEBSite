from django.urls import path
from apps.settings.views import IndexVIew, AboutView, PortfolioView, ServicesView

urlpatterns = [
    path("", IndexVIew.as_view(), name='index'),
    path("about", AboutView.as_view(), name="about"),
    path("portfolio", PortfolioView.as_view(), name="portfolio"),
    path("services", ServicesView.as_view(), name='services')
]
