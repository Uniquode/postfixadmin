
from nap import datamapper
from .models import Domain, Mailbox, Alias


class DomainMapper(datamapper.ModelDataMapper):

    class Meta:
        model = Domain
        fields = '__all__'


class MailboxMapper(datamapper.ModelDataMapper):

    class Meta:
        model = Mailbox
        fields = '__all__'


class AliasMapper(datamapper.ModelDataMapper):

    class Meta:
        model = Alias
        fields = '__all__'

