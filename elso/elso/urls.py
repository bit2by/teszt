from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('egy/', include('egy.urls')),
    path('admin/', admin.site.urls),
]
