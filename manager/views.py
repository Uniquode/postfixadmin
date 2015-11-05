from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .views_base import DomainView, MailboxView, AliasView, MapView


class HomeView(TemplateView):
    template_name = 'home.html'


class DomainCreateView(DomainView, CreateView):
    pass


class DomainUpdateView(DomainView, UpdateView):
    pass


class DomainDeleteView(DomainView, DeleteView):
    pass


class MailboxCreateView(MailboxView, CreateView):
    pass


class MailboxUpdateView(MailboxView, UpdateView):
    pass


class MailboxDeleteView(MailboxView, DeleteView):
    pass


class AliasCreateView(AliasView, CreateView):
    pass


class AliasUpdateView(AliasView, UpdateView):
    pass


class AliasDeleteView(AliasView, DeleteView):
    pass


class MapCreateView(MapView, CreateView):
    pass


class MapUpdateView(MapView, UpdateView):
    pass


class MapDeleteView(MapView, DeleteView):
    pass


