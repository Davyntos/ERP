from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Panel de administración nativo (Útil para el rol Administrativo)
    path('admin/', admin.site.urls),
    
    # Rutas para el flujo de autenticación (Login/Logout) de usuarios
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Rutas del corazón de tu ERP (La cascada de procesos)
    path('', include('apps.procesos.urls')), 
]

# Configuración para poder ver imágenes/archivos subidos por los usuarios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)