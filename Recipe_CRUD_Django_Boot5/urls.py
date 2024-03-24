from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path  # 👈 1. add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_project.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
