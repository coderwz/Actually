from django.shortcuts import render, render_to_response
from githubActually.models import Project, PM, Developer, Milestone, Section, Task, Commit
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain






def findPmByProject(GivenProject):
		findProject = Project.objects.filter(name = GivenProject)
		if (len(findProject) != 0):
			PmName= PM.objects.filter(project =findProject)
			return PmName 
		else:
			print 'no PM found by project'

def findDeveloperByProject(GivenProject):
	findProject = Project.objects.filter(name = GivenProject)
	if (len(findProject) != 0):
		DeveloperName = Developer.objects.filter(project = findProject)
		return DeveloperName
	else:
		print 'no Developer found by project'










def findProjectByPM(GivenPMID):
	findPM = PM.objects.get(id = GivenDeveloperID)
	findProject = findPM.project.all()
	if (len(findProject) != 0):
		return findProject
	else:
		print []


def findProjectByDeveloper(GivenDeveloperID):
		
		findDeveloper = Developer.objects.get(id = GivenDeveloperID)
		findProject = findDeveloper.project.all()
		if (len(findProject) != 0):
			return findProject
		else:
			print []


# def test(request):
# 	#data = Person.sdafasdf;
# 	#project name actually

#  	findDeveloper = Developer.objects.get(id =1)
# 	data = findDeveloper.project.all()
# 	return render_to_response('test.html',{'msg':data})






def findMilestonsByDeveloperProject(developerID,projectID):

	milestons = Milestone.objects.filter(project = projectID,developer = developerID)
	return milestons

def test(request):

 	data = findSectionByProjectIDDeveloperID(1,1)
	return render_to_response('test.html',{'msg':data})


def findSectionByProjectIDDeveloperID(projectID,developerID):
	section = Section.objects.get(project = projectID,developer = developerID)
	return section






# def findSectionByMilestoneID(milestoneID):

# 	findSectionByMilestone = Section.objects.filter(milestone = milestoneID)
# 	if (len(findSectionByMilestone) != 0):
# 		return findSectionByMilestone
# 	else:
# 		print 'error happening'



def findTasksBySectionID(sectionID):

	findTasksBySection = Task.objects.filter(section = sectionID)
	if (len(findTasksBySection) != 0):
		return findTasksBySection
	else:
		print 'error happening'



# def test(request):
# 	#data = Person.sdafasdf;
# 	#project name actually

# 	data = '1'

# 	return render_to_response('test.html',{'msg':data})




# def test(request):
# 	#data = Person.sdafasdf;
# 	#project name actually

#  	data = list(chain(findPmByProject('actually'),findDeveloperByProject('actually')))

# 	return render_to_response('test.html',{'msg':data})

# def test(request):
# 	#data = Person.sdafasdf;
# 	#project name actually

#  	data = list(chain(findProjectByPM('yj'),findProjectByDeveloper('ZW')))

# 	return render_to_response('test.html',{'msg':data})

# def test(request):
# 	#data = Person.sdafasdf;
# 	#project name actually

# 	data = findSectionByMilestone(1)

# 	return render_to_response('test.html',{'msg':data})