from django.contrib import admin
from django.urls import path, include

from api.urls import router


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
