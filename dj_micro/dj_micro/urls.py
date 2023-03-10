from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("users/", include("users.api.urls")),
    path('admin/', admin.site.urls),
]

if settings.URL_PREFIX:
    urlpatterns = [path(f'{settings.URL_PREFIX}/', include(urlpatterns))]
