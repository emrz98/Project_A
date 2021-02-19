from team_management import models
from django.contrib import admin

admin.site.register(models.resource_type)
admin.site.register(models.project_type)
admin.site.register(models.task_type)
admin.site.register(models.task_status)
admin.site.register(models.customer)
admin.site.register(models.comment_type)
admin.site.register(models.comments)
admin.site.register(models.resource)
admin.site.register(models.project)
admin.site.register(models.task)
