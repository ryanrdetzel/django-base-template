""" Default urlconf for {{ project_name }} """

from django.conf import settings
from django.conf.urls.defaults import include, patterns
from session_csrf import anonymous_csrf
from django.contrib import admin
from django.conf.urls.defaults import url, patterns
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', '{{ project_name }}.views.home', name='home'),
    #(r'^app_name/', include('app_name.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/$', anonymous_csrf(admin.site.admin_view(admin.site.index))),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^', include('debug_toolbar_user_panel.urls')),
)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
