
from nap import datamapper
from .models import Domain, Mailbox, Alias, Vacation, Admin


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


class VacationMapper(datamapper.ModelDataMapper):

    class Meta:
        model = Vacation
        fields = '__all__'
