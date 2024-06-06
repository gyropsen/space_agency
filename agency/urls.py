from django.urls import path

from agency.apps import AgencyConfig
from agency.views import StartPageTemplateView

app_name = AgencyConfig.name

urlpatterns = [
    path("", StartPageTemplateView.as_view(), name="start_page"),
]
