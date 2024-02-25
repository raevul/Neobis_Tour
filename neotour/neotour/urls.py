from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg import views, openapi
import os


schema_view = views.get_schema_view(
    openapi.Info(
        title="Tour API",
        default_version="v1",
        description="""In this project implemented reservation tour by category, season
        implemented leave a review, authentication, show tour list and tour detail
        """,
        terms_of_service="",
        contact=openapi.Contact(email=os.getenv('EMAIL')),
        license=openapi.License(name="BCD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include('tour.urls')),
    path('api/v1/', include('reserve.urls')),
    path('api/v1/', include('account.urls'))
]
