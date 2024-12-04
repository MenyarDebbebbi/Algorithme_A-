from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drone_app/', include('drone_app.urls')),
    path('', include('drone_app.urls')),
]
