from django.views.generic import ListView

from agency.models import Picture


class StartPageTemplateView(ListView):
    model = Picture
    extra_context = {
        "title": "Космическое агенство",
        "description": "Национальное управление по аэронавтике и исследованию космического пространства — ведомство, "
                       "относящееся к федеральному правительству США и подчиняющееся непосредственно президенту США."
    }
