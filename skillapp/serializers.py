from rest_framework import serializers
from .models import CustomUser, Skill, Enrollment, Review

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role']

class SkillSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField()

    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'instructor', 'running_time', 'max_students']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    skill = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'skill', 'date_enrolled']

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
    skill = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'skill', 'rating', 'comment']