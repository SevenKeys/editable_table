from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'web_app.views.home', name='home'),
    url(r'^', include('tables.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
