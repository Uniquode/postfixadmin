from django.conf import settings
from django.db import models


class Record(models.Model):
    """ common abstract class that manages creation and modification data """
    created = models.DateTimeField(verbose_name='Created on', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Last Modified', auto_now=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    class Meta:
        abstract = True


class Domain(Record):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)
    transport = models.CharField(max_length=255, blank=True)
    maxquota_mb = models.IntegerField(verbose_name='Max Quota', default=0)
    is_backup_mx = models.BooleanField(verbose_name='Backup MX', default=False)
    allow_mailbox = models.BooleanField(verbose_name='Allow New Mailboxes', default=True)
    auth_source = models.TextField(verbose_name='Authentication Source', blank=True)

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
    credential = models.TextField(verbose_name='Password', blank=True)
    name = models.CharField(verbose_name='Full Name', max_length=255)
    quota_mb = models.IntegerField(verbose_name='Quota', default=0)
    disposition = models.TextField(blank=True, null=True)
    vacation_enabled = models.BooleanField(default=False)
    vacation_subject = models.CharField(max_length=255, blank=True, null=True)
    vacation_body = models.TextField(blank=True, null=True)
    vacation_cache = models.TextField(editable=False, blank=True, null=True)

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


class Map(Record):
    """ Generic map definitions """
    name = models.CharField(verbose_name='Map Name', max_length=64, unique=True)
    fn1 = models.CharField(verbose_name='Field Name 1', max_length=64, default='Value')
    fn2 = models.CharField(verbose_name='Field Name 2', max_length=64, blank=True, null=True)
    fn3 = models.CharField(verbose_name='Field Name 3', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class MapValue(Record):
    """ Generic key->value mappings for maps """
    map = models.ForeignKey(Map)
    key = models.CharField(max_length=255)
    v1 = models.TextField(verbose_name='Value 1', blank=True)
    v2 = models.TextField(verbose_name='Value 2', blank=True, null=True)
    v3 = models.TextField(verbose_name='Value 3', blank=True, null=True)

    def __str__(self):
        return "{0}:{1}={2}".format(self.map, self.key,
                ':'.join([ x for x in (self.v1, self.v2, self.v3) if x is not None ]))
