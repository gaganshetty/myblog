from django.conf.urls import static,url,include
from django.conf import settings
from django.contrib import admin
from blogger import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogDetail.as_view(), name='details'),
    url(r'^admin/',include(admin.site.urls)),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)