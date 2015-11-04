from django.core.urlresolvers import reverse_lazy
from .models import Domain, Mailbox, Alias, Vacation
from .forms import DomainForm, MailboxForm, AliasForm, VacationForm


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


class VacationView(object):
    model = Vacation
    form_class = VacationForm
    success_url = reverse_lazy('vacations')

    def get_context_data(self, **kwargs):
        context = super(VacationView, self).get_context_data(**kwargs)
        context['vacation_list'] = Vacation.objects.all()
        return context
