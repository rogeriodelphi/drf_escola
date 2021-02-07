from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cursos.urls import router

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
