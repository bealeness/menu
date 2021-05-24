from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls', namespace='menu')),
    path('api/', include('menu_api.urls', namespace='menu_api')),
]
