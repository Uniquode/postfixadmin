from django import forms

from .models import Domain, Mailbox, Alias, Vacation


class DomainForm(forms.ModelForm):

    class Meta:
        model = Domain
        fields = ('name', 'description', 'transport', 'maxquota_mb', 'is_backup_mx', 'is_active')


class MailboxForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MailboxForm, self).__init__(*args, **kwargs)
        self.fields['credential'].widget.attrs['rows'] = 3
        self.fields['disposition'].widget.attrs['rows'] = 3
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            domain = self.fields['domain']
            domain.widget.attrs['readonly'] = True
            domain.widget.attrs['disabled'] = True
            domain.widget.is_required = False

    def clean_domain(self):
        domain = self.cleaned_data['domain']
        return domain

    class Meta:
        model = Mailbox
        fields = ('domain', 'username', 'name', 'credential', 'quota_mb', 'disposition', 'is_active')



class AliasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AliasForm, self).__init__(*args, **kwargs)
        self.fields['disposition'].widget.attrs['rows'] = 3
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['domain'].widget.attrs['readonly'] = True
            self.fields['domain'].widget.attrs['disabled'] = True

    def clean_domain(self):
        instance = getattr(self, 'instance', None)
        return instance.domain if instance and instance.pk else self.cleaned_data['domain']

    class Meta:
        model = Alias
        fields = ('domain', 'name', 'disposition', 'is_active')


class VacationForm(forms.ModelForm):
    domain = forms.ModelChoiceField(queryset=Domain.objects.all())

    def __init__(self, *args, **kwargs):
        super(VacationForm, self).__init__(*args, **kwargs)
        self.fields['response_body'].widget.attrs['rows'] = 6
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['domain'].widget.attrs['readonly'] = True
            self.fields['domain'].widget.attrs['disabled'] = True

    def clean_domain(self):
        instance = getattr(self, 'instance', None)
        return instance.domain if instance and instance.pk else self.cleaned_data['domain']

    class Meta:
        model = Vacation
        fields = ('domain', 'mailbox', 'response_subject', 'response_body', 'is_active')
