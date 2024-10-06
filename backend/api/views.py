from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Course, CourseStudent, Lesson, VideoMaterial, \
    TextMaterial
from . import serializers


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    pagination_class = None


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer
    pagination_class = None


class CourseStudentViewSet(viewsets.ModelViewSet):
    queryset = CourseStudent.objects.all()
    serializer_class = serializers.CourseStudentSerializer
    pagination_class = None


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    pagination_class = None


class VideoMaterialViewSet(viewsets.ModelViewSet):
    queryset = VideoMaterial.objects.all()
    serializer_class = serializers.VideoMaterialSerializer
    pagination_class = None


class TextMaterialViewSet(viewsets.ModelViewSet):
    queryset = TextMaterial.objects.all()
    serializer_class = serializers.TextMaterialSerializer
    pagination_class = None


