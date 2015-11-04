from django.conf import settings
from django.db import models


class Record(models.Model):
    """ common abstract class that manages creation and modification data """
    created = models.DateTimeField(verbose_name='Created on', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Last Modified', auto_now=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    class Meta:
        abstract = True


class Admin(Record):
    """ administrative users """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @classmethod
    def create_admin_for_user(cls, user):
        """ shortcut method to create a user from a given user model """
        admin = Admin(user=user, is_active=True)
        admin.save()
        return admin

    def __str__(self):
        return self.user.name


class Domain(Record):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)
    transport = models.CharField(max_length=255, blank=True)
    maxquota_mb = models.IntegerField(verbose_name='Max Quota', default=0)
    is_backup_mx = models.BooleanField(verbose_name='Backup MX', default=False)

    @classmethod
    def at_domain(cls, domain=None):
        return '@{0}'.format(domain) if domain else ''

    @property
    def aliases(self):
        return self.alias_set.count()

    @property
    def mailboxes(self):
        return self.mailbox_set.count()

    def __str__(self):
        return self.name


class Mailbox(Record):
    """ Mailboxes """
    domain = models.ForeignKey(Domain, null=True)
    username = models.CharField(max_length=255)
    credential = models.TextField(verbose_name='Password')
    name = models.CharField(verbose_name='Full Name', max_length=255)
    quota_mb = models.IntegerField(verbose_name='Quota', default=0)
    disposition = models.TextField(blank=True, null=True)

    @property
    def address(self):
        return '{0}{1}'.format(self.username, Domain.at_domain(self.domain))

    def __str__(self):
        return self.address

    class Meta:
        unique_together = ('domain', 'username',)


class Alias(Record):
    """ email aliases """
    domain = models.ForeignKey(Domain, null=True)
    name = models.CharField(max_length=255)
    disposition = models.TextField()

    @property
    def address(self):
        return '{0}{1}'.format(self.name, Domain.at_domain(self.domain))

    def __str__(self):
        return self.address

    class Meta:
        unique_together = ('domain', 'name',)


class Vacation(Record):
    """ vacation records """
    mailbox = models.OneToOneField(Mailbox)
    response_subject = models.CharField(max_length=255)
    response_body = models.TextField()
    cache = models.TextField(editable=False)

    @property
    def domain(self):
        return self.mailbox.domain if self.mailbox else None

    class Meta:
        unique_together = ('mailbox',)
