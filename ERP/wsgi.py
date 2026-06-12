import os
from django.core.wsgi import get_wsgi_application

# Configura el módulo de ajustes por defecto para tu ERP
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_erp_project.settings')

application = get_wsgi_application()