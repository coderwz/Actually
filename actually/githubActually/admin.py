from django.contrib import admin
from githubActually.models import Project, User, Milestone, Section, Task, Commit
# Register your models here.
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Milestone)
admin.site.register(Section)
admin.site.register(Task)
admin.site.register(Commit)
