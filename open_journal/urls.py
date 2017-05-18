"""open_journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from journal.views import journal_write, journal_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', journal_write, name='write'),
	url(r'^entry/(?P<entry_id>[0-9]+)/$', journal_detail, name='detail'),
    url(r'^admin/', admin.site.urls),
    # Url Entries for social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    # Url Entries for django administration
    url('', include('django.contrib.auth.urls', namespace='auth')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # NOT FOR PRODUCTION
