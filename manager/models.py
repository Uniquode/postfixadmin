from django.conf import settings
from django.db import models


class Record(models.Model):
    """ common abstract class that manages creation and modification data """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Admin(Record):
    """ administrative users """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @classmethod
    def create_admin_for_user(cls, user):
        """ shortcut method to create a user from a given user model """
        admin = Admin(user=user)
        admin.save()
        return admin


class Alias(Record):
    """ email aliases """
    address = models.CharField(max_length=255)
    goto = models.TextField()
