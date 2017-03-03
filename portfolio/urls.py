# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'portfolio.views.index', name='index'),
    url(r'^o-mnie/$', 'portfolio.views.about', name='about'),
    url(r'^oferta/$', 'portfolio.views.offer', name='offer'),
    url(r'^kontakt/$', 'portfolio.views.contact', name='contact'),
    #url(r'^admin/', include(admin.site.urls)),
    
)
#ERRORS:
handler404 = 'portfolio.views.error404'
handler500 = 'portfolio.views.error500'
handler403 = 'portfolio.views.error403'
handler400 = 'portfolio.views.error403'