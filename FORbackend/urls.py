from django.contrib import admin
from django.conf.urls import url, include
from .api import router
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^token-auth/', views.obtain_auth_token),
    url(r'^api/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
]
