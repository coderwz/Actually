from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Users include developers and product managers
# give github name , return projects
# give project , return all users, and pm( at top of list)
# give a github name, return all milestones 

class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	startTime = models.DateTimeField('date the project starts')
	finishTime = models.DateTimeField('date the project finishes', null = True, blank = True)
	progress = models.FloatField(default = 0)
	prevProgress =models.FloatField(default = 0)


	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = progress

	def findPmDeveloperByProject(self,GivenProject):
		findPM = Project.objects.filter(name = GivenProject)
		return 


class PM(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	githubName = models.CharField(max_length =50)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def __unicode__(self):
		return '{} {}'.format(self.firstName, self.lastName)



class Developer(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	githubName = models.CharField(max_length =50, null = True, blank =True)
	pmAssigned = models.ForeignKey(PM, null = True, blank = True)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def findProjectByUser(self, GivenGithub_name):
		#many to many
		findDevloper = Project.objects.filter(githubName=GivenGithub_name)
		return findDevloper

class Milestone(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	progress = models.FloatField(default = 0)
	prevProgress = models.FloatField(default = 0)
	percentage = models.FloatField()
	dueDate = models.DateTimeField()

	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.prevProgress = self.progress
		section = Section.objects.all()
		prog = 0
		for sec in section:
			prog = prog + sec.percentage
		self.progress = self.progress + progress/prog

class Section(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the project')
	progress = models.FloatField(default = 0)
	prevProgress = models.FloatField(default = 0)
	developer = models.ForeignKey(Developer, null = True, blank = True)
	project = models.ForeignKey(Project)
	milestone = models.ForeignKey(Milestone)

	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = self.progress + progress
		progressUpdate = self.percentage * progress 
		self.project.update(progressUpdate)

class Task(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the section')
	progress = models.FloatField(default = 0)
	prevProgress = models.FloatField(default = 0)
	section = models.ForeignKey(Section)

	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = progress
		updateProgress = self.percentage * (self.progress - self.prevProgress)
		self.section.update(updateProgress)

	def __unicode__(self):
		return self.name

class Commit(models.Model):
	commitTime = models.DateTimeField()
	progress = models.FloatField()
	developer = models.ForeignKey(Developer)
	task = models.ForeignKey(Task)

	def __unicode__(self):
		return '{} {} {} {:.2f} {}'.format(self.developer.firstName, self.developer.lastName, 
			self.task.name, self.progress, self.commitTime)






















