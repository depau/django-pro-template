from django.shortcuts import redirect
from drf_spectacular.plumbing import get_relative_url, set_query_parameters
from drf_spectacular.settings import spectacular_settings
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import AUTHENTICATION_CLASSES
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.views import APIView


class SpectacularRapidocView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = spectacular_settings.SERVE_PERMISSIONS
    authentication_classes = AUTHENTICATION_CLASSES
    url_name = "schema"
    url = None
    template_name = "rapidoc.html"
    title = spectacular_settings.TITLE

    @extend_schema(exclude=True)
    def get(self, request, *_args, **_kwargs):
        schema_url = self.url or get_relative_url(reverse(self.url_name, request=request))
        schema_url = set_query_parameters(schema_url, lang=request.GET.get("lang"))
        return Response(
            data={
                "title": self.title,
                "dist": "https://cdn.jsdelivr.net/npm/rapidoc@latest",
                "schema_url": schema_url,
            },
            template_name=self.template_name,
        )


class SpectacularElementsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = spectacular_settings.SERVE_PERMISSIONS
    authentication_classes = AUTHENTICATION_CLASSES
    url_name = "schema"
    url = None
    template_name = "elements.html"
    title = spectacular_settings.TITLE

    @extend_schema(exclude=True)
    def get(self, request, *_args, **_kwargs):
        schema_url = self.url or get_relative_url(reverse(self.url_name, request=request))
        schema_url = set_query_parameters(
            schema_url, lang=request.GET.get("lang"), version=request.GET.get("version")
        )
        return Response(
            data={
                "title": self.title,
                "js_dist": "https://unpkg.com/@stoplight/elements/web-components.min.js",
                "css_dist": "https://unpkg.com/@stoplight/elements/styles.min.css",
                "schema_url": schema_url,
            },
            template_name=self.template_name,
        )


def apidocs(_request):
    return redirect(reverse_lazy("rapidoc-ui"))
