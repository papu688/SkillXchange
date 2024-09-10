
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('skillapp.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns += doc_urls