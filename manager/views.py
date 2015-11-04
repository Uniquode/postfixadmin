from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .views_base import DomainView, MailboxView, AliasView, VacationView

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


class VacationCreateView(VacationView, CreateView):
    pass


class VacationUpdateView(VacationView, UpdateView):
    pass


class VacationDeleteView(VacationView, DeleteView):
    pass

