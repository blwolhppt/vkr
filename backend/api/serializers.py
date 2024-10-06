from rest_framework import serializers

from .models import Teacher, Course, CourseStudent, Lesson, VideoMaterial, \
    TextMaterial


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class VideoMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = '__all__'


class TextMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMaterial
        fields = '__all__'

