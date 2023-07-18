from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from posts.viewset_api import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet)




urlpatterns = [
    path('api/', include(router.urls)),

    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

