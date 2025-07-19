from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_django_app.urls')),  # this makes the full URL "/api/add-user/"
]