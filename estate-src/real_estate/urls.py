from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('supersecret/', admin.site.urls),
    path('api/v1/auth/', include("djoser.urls")),  # Correct this line
    path('api/v1/auth/', include("djoser.urls.jwt")),  # Correct this line
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to Real Estate Portal"
