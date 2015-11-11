from django.core.urlresolvers import reverse_lazy
from .models import Domain, Mailbox, Alias, Map, MapValue
from .forms import DomainForm, MailboxForm, AliasForm, MapForm, MapValueForm


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


class MapValuesView(object):
    model = MapValue
    form_class = MapValueForm
    success_url = reverse_lazy('map_values')

    def get_success_url(self):
        return self.success_url + str(self.object.map.id)

    def get_context_data(self, **kwargs):
        context = super(MapValuesView, self).get_context_data(**kwargs)
        # See if we are being invoked for a specific map
        map_id = context['view'].kwargs.get('map_id')
        if not map_id:
            # If not, get the first map (if it exists)
            map = Map.objects.first()
            if map:
                map_id = map.id
                context['map_id'] = map_id
        else:
            map = Map.objects.get(id=map_id)
        # save this for success url
        self.map_id = map_id
        context['map'] = map
        # 'map' in the context is now set to the map that owns these key/values
        if 'form' in context:
            # Set the map field as appropriate
            context['form'].fields['map'].initial = map_id
            # And filter the list for this map (or empty if no map)
            context['value_list'] = MapValue.objects.filter(map_id=map_id)
            # Trim the values and override the field names as appropriate
            if not map.fn3:
                del context['form'].fields['v3']
            else:
                context['form'].fields['v3'].label = map.fn3
            if not map.fn2:
                del context['form'].fields['v2']
            else:
                context['form'].fields['v2'].label = map.fn2
            context['form'].fields['v1'].label = map.fn1
        return context


