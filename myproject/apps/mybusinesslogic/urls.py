from django.urls import URLPattern, URLResolver

app_name = __name__.rsplit(".", 1)[0]

urlpatterns: list[URLResolver | URLPattern] = []
