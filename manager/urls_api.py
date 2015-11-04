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
from . import views_api as views

urlpatterns = [
    url(r'^domain/$', views.ApiDomainListView.as_view()),
#   url(r'^api/domain/(?P<pk>\d+)/edit$', views.DomainUpdateView.as_view(), name='domain_edit'),
#   url(r'^api/domain/(?P<pk>\d+)/del$', views.DomainDeleteView.as_view(), name='domain_delete'),
    url(r'^mailbox/$', views.ApiMailboxListView.as_view()),
#   url(r'^api/mailbox/(?P<pk>\d+)/edit$', views.MailboxUpdateView.as_view(), name='mailbox_edit'),
#   url(r'^api/mailbox/(?P<pk>\d+)/del$', views.MailboxDeleteView.as_view(), name='mailbox_delete'),
    url(r'^alias/$', views.ApiAliasListView.as_view()),
#   url(r'^api/alias/(?P<pk>\d+)/edit$', views.AliasUpdateView.as_view(), name='alias_edit'),
#   url(r'^api/alias/(?P<pk>\d+)/del$', views.AliasDeleteView.as_view(), name='alias_delete'),
    url(r'^vacation/$', views.ApiVacationListView.as_view()),
#   url(r'^api/vacation/(?P<pk>\d+)/edit$', views.VacationUpdateView.as_view(), name='vacation_edit'),
#   url(r'^api/vacation/(?P<pk>\d+)/del$', views.VacationDeleteView.as_view(), name='vacation_delete'),
]
