from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# For linking up with app URLs file
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
