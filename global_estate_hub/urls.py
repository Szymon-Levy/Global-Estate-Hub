"""
URL configuration for global_estate_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path(route="ckeditor", view=include(arg="ckeditor_uploader.urls")),
    path(route="", view=include(arg="core.urls")),
    path(route="", view=include(arg="accounts.urls")),
    path(route="", view=include(arg="blog.urls")),
    path(route="", view=include(arg="properties.urls")),
    path(route="", view=include(arg="properties.api.urls")),
    path(route="", view=include(arg="accounts.api.urls")),
    path(route="", view=include(arg="core.api.urls")),
    path(route="", view=include(arg="blog.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
