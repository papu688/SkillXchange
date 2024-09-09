from rest_framework import permissions
from .models import CustomUser

class isAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        # Administrators have access to all actions
        return request.user.is_authenticated and request.user.role == CustomUser.ADMINISTRATOR
    
class CanAddSkill(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only authenticated instructors to add skills
        return request.user.is_authenticated and request.user.role == CustomUser.INSTRUCTOR
    
class CanDeleteSkill(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow instructors to delete their own skills only
        return request.user.is_authenticated and request.user.role == CustomUser.INSTRUCTOR and obj.tutor == request.user
    
class CanUpdateSkill(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow instructors to update their own skills only
        return request.user.is_authenticated and request.user.role == CustomUser.INSTRUCTOR and obj.tutor == request.user

class CanJoinSkill(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only authenticated students to join skills or add feedback
        return request.user.is_authenticated and request.user.role == CustomUser.STUDENT

    
