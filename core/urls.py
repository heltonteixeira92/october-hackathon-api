from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='HackathonAPI')),
    path('schema', get_schema_view(
        title='October Hackathon',
        description='October Hackathon API Edition',
        version='1.0.0'
    ), name='openapi-schema'),
]
