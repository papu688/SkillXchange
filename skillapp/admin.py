from django.contrib import admin
from .models import CustomUser, Skill, Enrollment, Review


admin.site.register(CustomUser)
admin.site.register(Skill)
admin.site.register(Enrollment)
admin.site.register(Review)