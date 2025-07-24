from django.contrib import admin
from django.urls import path, include
from edtech_api.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('edtech_api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
