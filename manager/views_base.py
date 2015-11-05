from django.core.urlresolvers import reverse_lazy
from .models import Domain, Mailbox, Alias, Map
from .forms import DomainForm, MailboxForm, AliasForm, MapForm


class DomainView(object):
    model = Domain
    form_class = DomainForm
    success_url = reverse_lazy('domains')

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        context['domain_list'] = Domain.objects.all()
        return context


class MailboxView(object):
    model = Mailbox
    form_class = MailboxForm
    success_url = reverse_lazy('mailboxes')

    def get_context_data(self, **kwargs):
        context = super(MailboxView, self).get_context_data(**kwargs)
        context['mailbox_list'] = Mailbox.objects.all()
        return context


class AliasView(object):
    model = Alias
    form_class = AliasForm
    success_url = reverse_lazy('aliases')

    def get_context_data(self, **kwargs):
        context = super(AliasView, self).get_context_data(**kwargs)
        context['alias_list'] = Alias.objects.all()
        return context


class MapView(object):
    model = Map
    form_class = MapForm
    success_url = reverse_lazy('maps')

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context['map_list'] = Map.objects.all()
        return context
