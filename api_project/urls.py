from django.contrib import admin
from django.urls import path, include   # include is important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # now Django knows to look inside api/urls.py
]
