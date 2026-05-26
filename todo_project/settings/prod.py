from .base import *


DEBUG = False


ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

# Безпека для продакшену
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True