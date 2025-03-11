"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
]