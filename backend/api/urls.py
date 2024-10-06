from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('teachers', views.TeacherViewSet)
router.register('courses', views.CourseViewSet)
router.register('coursestudents', views.CourseStudentViewSet)
router.register('videomaterials', views.VideoMaterialViewSet)
router.register('textmaterials', views.TextMaterialViewSet)
router.register('lessons', views.LessonViewSet)


urlpatterns = [
    path('', include(router.urls)),
]