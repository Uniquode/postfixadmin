"""
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^domain/$', views.DomainCreateView.as_view(), name='domains'),
    url(r'^domain/(?P<pk>\d+)/edit$', views.DomainUpdateView.as_view(), name='domain_edit'),
    url(r'^domain/(?P<pk>\d+)/del$', views.DomainDeleteView.as_view(), name='domain_delete'),
    url(r'^mailbox/$', views.MailboxCreateView.as_view(), name='mailboxes'),
    url(r'^mailbox/(?P<pk>\d+)/edit$', views.MailboxUpdateView.as_view(), name='mailbox_edit'),
    url(r'^mailbox/(?P<pk>\d+)/del$', views.MailboxDeleteView.as_view(), name='mailbox_delete'),
    url(r'^alias/$', views.AliasCreateView.as_view(), name='aliases'),
    url(r'^alias/(?P<pk>\d+)/edit$', views.AliasUpdateView.as_view(), name='alias_edit'),
    url(r'^alias/(?P<pk>\d+)/del$', views.AliasDeleteView.as_view(), name='alias_delete'),
    url(r'^map/$', views.MapCreateView.as_view(), name='maps'),
    url(r'^map/(?P<pk>\d+)/edit$', views.MapUpdateView.as_view(), name='map_edit'),
    url(r'^map/(?P<pk>\d+)/del$', views.MapDeleteView.as_view(), name='map_delete'),
]
