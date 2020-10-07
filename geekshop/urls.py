from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("products/", mainapp.products, name="products"),
    path("products/all", mainapp.products, name="products_all"),
    path("products/home", mainapp.products, name="products_home"),
    path("products/office", mainapp.products, name="products_office"),
    path("products/modern", mainapp.products, name="products_modern"),
    path("products/classic", mainapp.products, name="products_classic"),
    path("contact/", mainapp.contact, name="contact"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)