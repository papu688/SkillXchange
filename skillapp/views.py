from rest_framework import viewsets
from .models import CustomUser, Skill, Enrollment, Review
from .serializers import CustomUserSerializer, SkillSerializer, EnrollmentSerializer, ReviewSerializer
from .permissions import isAdministrator, CanAddSkill, CanUpdateSkill, CanDeleteSkill, CanJoinSkill


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [CanAddSkill]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [CanUpdateSkill]
        elif self.action in ['destroy']:
            permission_classes = [CanDeleteSkill]
        else:
            # Allow all authenticated users to view the list and details
            permission_classes = [isAdministrator | CanJoinSkill]

        return [permission() for permission in permission_classes]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [CanJoinSkill]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [CanJoinSkill]
