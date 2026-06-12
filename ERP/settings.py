import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURIDAD: En desarrollo mantener True, pero cambiar a False en producción en el servidor
DEBUG = True

SECRET_KEY = 'django-insecure-cambia-esta-clave-por-una-segura-en-produccion'

ALLOWED_HOSTS = ['*'] # En producción coloca la IP de tu servidor o tu dominio (ej. ['tu-erp.com'])


# APPS DEL PROYECTO
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Tus aplicaciones locales
    'apps.core',
    'apps.procesos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Protección de seguridad nativa
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_erp_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Indicamos a Django que busque plantillas globales en una carpeta raíz si es necesario
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_erp_project.wsgi.application'


# CONFIGURACIÓN DE BASE DE DATOS (Conexión a MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_datos_erp',
        'USER': 'tu_usuario_mysql',
        'PASSWORD': 'tu_contrasena_mysql',
        'HOST': '127.0.0.1', # O 'localhost'
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# VALIDACIÓN DE CONTRASEÑAS (Seguridad de fábrica)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# IDIOMA Y ZONA HORARIA (Ajusta 'America/Bogota' por tu zona horaria local)
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# ARCHIVOS ESTÁTICOS Y MULTIMEDIA (Clave para Nginx en el servidor)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REDIRECCIONES DE LOGIN
LOGIN_REDIRECT_URL = '/'  # A dónde va el usuario tras iniciar sesión
LOGOUT_REDIRECT_URL = '/accounts/login/' # A dónde va al cerrar sesión