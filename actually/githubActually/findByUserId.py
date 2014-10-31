from models import PM, Developer, Project, Milestone, Section, Task, Commit

def findDeveloper(self, developerId):
	return Developer.objects.get(pk = developerId)

def findPM(self, pmId):
	return PM.objects.get(pk = pmId)

def findProjectsAssingedToDeveloper(self, developerId):
	return PM.objects.filter(developer = developerId).project

def findProjectsBelongedToPM(self, pmId):
	return PM.objects.filter(pm = pmId).project

def findSectionAssignedToDeveloper(self, projectId, developerId):
	return PM.objects.filter(project = projectId, developer = developerId)

def findTaskAssignedToDeveloper(self, projectId, developerId):
	sections = findSectionAssignedToDeveloper(self, projectId, developerId)
	return Task.objects.filter(section = sections)

def findCommitByTheDeveloper(self, project, developerId):
	

