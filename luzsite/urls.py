from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from luzgallery import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'luzsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.GalleryListView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<title>[\w-]+)/$', views.ImageListView.as_view()),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns
