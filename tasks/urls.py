from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet, TaskViewSet

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
from rest_framework import routers
from .views import CategoryViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls
