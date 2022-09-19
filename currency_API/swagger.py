from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Currency API",
        default_version="v1",
        description="This project parses currency price data in Ukraine and distributes them via API (json format)",
    ),
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    public=True,
)

swagger_pattern = path(
    "swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
)
