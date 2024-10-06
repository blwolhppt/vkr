from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('teacher', views.TeacherViewSet)
router.register('course', views.CourseViewSet)
router.register('coursestudent', views.CourseStudentViewSet)
router.register('videomaterial', views.VideoMaterialViewSet)
router.register('textmaterial', views.TextMaterialViewSet)
router.register('lesson', views.LessonViewSet)


urlpatterns = [
    path('', include(router.urls)),
]