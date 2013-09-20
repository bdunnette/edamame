from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
<<<<<<< HEAD
# from django.contrib import admin
# admin.autodiscover()
=======
from django.contrib import admin
admin.autodiscover()
>>>>>>> 93d600a0bd53b345ae52d62f1f6041032b563b84

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'edamame.views.home', name='home'),
    # url(r'^edamame/', include('edamame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
<<<<<<< HEAD
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
=======
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
>>>>>>> 93d600a0bd53b345ae52d62f1f6041032b563b84
)
