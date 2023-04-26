from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from backend import settings
from django.conf.urls.static import static
import users.urls as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('', include(users, namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
