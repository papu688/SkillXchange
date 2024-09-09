from django.db import models 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMINISTRATOR = 'administrator'
    INSTRUCTOR = 'instructor' 
    STUDENT = 'student'
    ROLE_CHOICES = [
        (ADMINISTRATOR, 'administrator'),
        (INSTRUCTOR, 'instructor'),
        (STUDENT, 'student'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=STUDENT)

    def __str__(self):
        return self.username

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    instructor = models.ForeignKey(CustomUser, limit_choices_to={'role': 'instructor'}, on_delete=models.CASCADE)
    running_times = models.CharField(max_length=100) #for example, 'Monday, Wednesday 9 AM 1 AM'
    max_students = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.skill.name}'
    
class Review(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(CustomUser, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1 to 5 rating
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.reviewer.username} for {self.skill.name}'
    


