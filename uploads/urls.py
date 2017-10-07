from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^Create_roject/$', views.Create_roject, name='Create_roject'),
    url(r'^Create_ToDo/$', views.Create_ToDo, name='Create_ToDo'),
    url(r'^Upload_Files/$', views.Upload_Files, name='Upload_Files'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
