from django.urls import path
from apps.settings.views import IndexVIew

urlpatterns = [
    path("", IndexVIew.as_view(), name='index'),
]
