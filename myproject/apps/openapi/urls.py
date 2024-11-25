from django.urls import path
from drf_spectacular.views import SpectacularAPIView

from myproject.apps.openapi.views import SpectacularElementsView, SpectacularRapidocView, apidocs

urlpatterns = [
    path("", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", apidocs, name="apidocs"),
    path(
        "rapidoc/",
        SpectacularRapidocView.as_view(url_name="schema"),
        name="rapidoc-ui",
    ),
    path(
        "elements/",
        SpectacularElementsView.as_view(url_name="schema"),
        name="elements-ui",
    ),
]
