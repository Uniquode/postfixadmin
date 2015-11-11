from django import forms
from django.core.exceptions import ValidationError

from .models import Domain, Mailbox, Alias, Map, MapValue


class DomainForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DomainForm, self).__init__(*args, **kwargs)
        self.fields['auth_source'].widget.attrs['rows'] = 2

    class Meta:
        model = Domain
        fields = ('name', 'description', 'transport', 'maxquota_mb',
                  'auth_source',
                  'is_backup_mx', 'allow_mailbox', 'is_active')


class MailboxForm(forms.ModelForm):
    domain = forms.ModelChoiceField(
        queryset=Domain.objects.filter(is_active=True, is_backup_mx=False), initial=2
    )

    def __init__(self, *args, **kwargs):
        super(MailboxForm, self).__init__(*args, **kwargs)
        self.fields['vacation_body'].widget.attrs['rows'] = 6

    def clean(self):
        if not self.instance.pk:
            domain = self.cleaned_data['domain']
            if not domain.allow_mailbox:
                raise ValidationError("Cannot create new mailboxes for domain '%s'" % (domain.name,))

    class Meta:
        model = Mailbox
        fields = ('domain', 'username', 'name', 'credential', 'quota_mb',
                  'disposition',
                  'vacation_enabled', 'vacation_subject', 'vacation_body',
                  'is_active' )
        widgets = {
            'credential': forms.TextInput(),
            'disposition': forms.TextInput(),
        }


class AliasForm(forms.ModelForm):
    domain = forms.ModelChoiceField(
        queryset=Domain.objects.filter(is_active=True, is_backup_mx=False), initial=2
    )

    def __init__(self, *args, **kwargs):
        super(AliasForm, self).__init__(*args, **kwargs)
        self.fields['disposition'].widget.attrs['rows'] = 3

    def clean_domain(self):
        instance = getattr(self, 'instance', None)
        return instance.domain if instance and instance.pk else self.cleaned_data['domain']

    class Meta:
        model = Alias
        fields = ('domain', 'name', 'disposition', 'is_active')


class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = ('name', 'fn1', 'fn2', 'fn3', 'is_active')


class MapValueForm(forms.ModelForm):
    map = forms.ModelChoiceField(queryset=Map.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super(MapValueForm, self).__init__(*args, **kwargs)
        self.fields['v1'].widget.attrs['rows'] = 1
        self.fields['v2'].widget.attrs['rows'] = 1
        self.fields['v3'].widget.attrs['rows'] = 1

    class Meta:
        model = MapValue
        fields = ('map', 'key', 'v1', 'v2', 'v3')
        widgets = {
            'v1': forms.TextInput(),
            'v2': forms.TextInput(),
            'v3': forms.TextInput(),
        }
