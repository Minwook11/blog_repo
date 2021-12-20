from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_prac.views import PracticeViewSet

router = routers.DefaultRouter()
router.register('practice', PracticeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('base.urls')),
	path('', include(router.urls)),
]
