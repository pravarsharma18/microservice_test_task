from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("users/", include("users.api.urls")),
    path('admin/', admin.site.urls),
]
