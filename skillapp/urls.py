from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, EnrollmentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]