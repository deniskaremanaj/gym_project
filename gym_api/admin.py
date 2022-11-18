from django.contrib import admin
from gym_api import models

admin.site.register(models.MemberProfile)
admin.site.register(models.InstructorProfile)
admin.site.register(models.UserFeedItem)
