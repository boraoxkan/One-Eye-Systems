# oneeye_website/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Dil çevirisine dahil EDİLMEYECEK URL'ler
urlpatterns = [
    path('admin/', admin.site.urls),
    # Bu satırı ekleyerek Django'nun dil değiştirme URL'ini aktif edin
    path('i18n/', include('django.conf.urls.i18n')),
]

# Dil çevirisine dahil EDİLECEK URL'ler
urlpatterns += i18n_patterns(
    path('', include('main.urls', namespace='main')),
)

# Geliştirme ortamında media dosyalarını sunmak için
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)