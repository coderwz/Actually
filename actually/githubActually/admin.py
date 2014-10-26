from django.contrib import admin
from githubActually.models import Project, User, Milestone, Section, Task, Commit
# Register your models here.
# class UserInline(admin.StackedInline):
# 	model = Project.user.through
# 	extra = 3

class ProjectAdmin(admin.ModelAdmin):
	pass
# 	inlines = [UserInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(User)
admin.site.register(Milestone)
admin.site.register(Section)
admin.site.register(Task)
admin.site.register(Commit)
