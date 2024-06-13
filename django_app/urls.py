from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # Include the CKEditor 5 URLs
    path('', include('blog.urls')),  # Include your blog app URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
