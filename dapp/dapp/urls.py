from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets, routers
from rest_framework.authtoken import views

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User    
        fields = ['url', 'username', 'email', 'is_staff']     
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  
           
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('post_app.urls', namespace="post_app")),
    path('api-token-auth/', views.obtain_auth_token),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('core.urls', namespace="core")),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)