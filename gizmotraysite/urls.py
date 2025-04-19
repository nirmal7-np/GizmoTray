from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.custom_admin_site import custom_admin_site
from store.views import custom_admin_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),  # Default admin (optional)
    path('dashboard/', custom_admin_site.urls),   # ✅ Custom Admin
    path('', include('store.urls')),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
