from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
