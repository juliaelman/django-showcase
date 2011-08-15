from django.contrib import admin
from showcase.models import Project, ProjectType, Client, ProjectImage, Role

admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(ProjectImage)
admin.site.register(Client)
admin.site.register(Role)
