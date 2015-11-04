from nap.rest.views import BaseListView, ListGetMixin

from .models import Domain, Mailbox, Alias, Vacation
from .mappers import DomainMapper, MailboxMapper, AliasMapper, VacationMapper
from .views_base import DomainView, MailboxView, AliasView, VacationView

# Endpoints
# 01. list domains (name contains)
# 02. list mailboxes (by domain, username contains)
# 03. list aliases (by domain, alias contains)
# 04. list vacation records (by domain, username contains)


class ApiDomainListView(ListGetMixin, BaseListView):
    model = Domain
    mapper_class = DomainMapper

    def dispatch(self, request, *args, **kwargs):
        return super(ApiDomainListView, self).dispatch(request, *args, **kwargs)


class ApiMailboxListView(ListGetMixin, BaseListView):
    model = Mailbox
    mapper_class = MailboxMapper


class ApiAliasListView(ListGetMixin, BaseListView):
    model = Alias
    mapper_class = AliasMapper


class ApiVacationListView(ListGetMixin, BaseListView):
    model = Vacation
    mapper_class = VacationMapper

