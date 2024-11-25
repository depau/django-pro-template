"""URL configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

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

import textwrap

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


# REMOVE THIS VIEW WHEN YOU ADD YOUR OWN VIEWS
def demo_view(request):
    return HttpResponse(
        textwrap.dedent("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Django Professional Multi-site Template</title>
            <style>
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    font-family: Arial, sans-serif;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Django Professional Multi-site Template</h1>
                <p>If you see this page it means you successfully set up your starter project.</p>
                <p>You can now follow the instructions in <a href="https://github.com/depau/django-pro-multisite-template">the GitHub page</a> to make it yours.</p>
                <div>
                <h2>Things to check out:</h2>
                <ul>
                    <li>The <a href="/admin/">Django Admin</a></li>
                    <li><a href="/api/schema/docs/">OpenAPI documentation</a> (using <a href="https://rapidocweb.com/" target="_blank" rel="noopener">RapiDoc</a>)</li>
                    <li><a href="/api/schema/elements/">OpenAPI documentation</a> (using <a href="https://github.com/stoplightio/elements" target="_blank" rel="noopener">Elements</a>)</li>
                    <li>The <a href="/health/">Health status page</a></li>
                    <li>The <a href="/api/v1/core/">DRF built-in API viewer</a> for the core app</li>
                    <li>The Django Debug Toolbar (look on the right)</li>
                </ul>
                </div>
            </div>
        </body>
        </html>
    """).strip()
    )


urlpatterns = [
    path("", demo_view, name="demo"),  # REMOVE THIS LINE WHEN YOU ADD YOUR OWN VIEWS
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/v1/core/",
        include("myproject.apps.core.api_urls", namespace="myproject.apps.core:v1"),
    ),
    path(
        "api/v1/mybusinesslogic/",
        include(
            "myproject.apps.mybusinesslogic.api_urls", namespace="myproject.apps.mybusinesslogic:v1"
        ),
    ),
    path("api/schema/", include("myproject.apps.openapi.urls")),
    path("health/", include("health_check.urls")),
]

if settings.DEBUG and not settings.TESTING:
    urlpatterns.extend(debug_toolbar_urls())
