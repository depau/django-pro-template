from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = __name__.rsplit(".", 1)[0]

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
]
