from django.contrib import admin
from django.urls import path, include

from main.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),

]
