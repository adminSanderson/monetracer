from django.urls import path, include
from main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    path("", views.index, name='index'),
    # path("navigation/", views.navigation, name='navigation'),
    # path("tracer/", views.tracer, name='tracer'),
    path("analytics/", views.analytics, name='analytics'),
    path("about/", views.about, name='about'),
    path('admin/', admin.site.urls),
    path("iapp/", include('iapp.urls')),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
