from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from publications.views import PublicationViewSet, CommentViewSet
from users.views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename="users")
router.register('publications', PublicationViewSet, basename='publications')

publications_comments_router = routers.NestedSimpleRouter(router, 'publications', lookup='publication')
publications_comments_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls + publications_comments_router.urls))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
