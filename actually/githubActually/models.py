from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# Users include developers and product managers
class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	startTime = models.DateTimeField('date the project starts')
	finishTime = models.DateTimeField('date the project finishes', null = True, blank = True)
	progress = models.FloatField(default = 0)
	prevProgress =models.FloatField(default = 0)

	# def __init__(self, name, description, startTime):
	# 	self.name = name
	# 	self.description = description
	# 	self.startTime = startTime
	# 	self.progress = 0

	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = progress



class PM(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	githubName = models.CharField(max_length =50)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def __unicode__(self):
		return '{} {}'.format(self.firstName, self.lastName)

	def __init__(self, name, githubName, project):
		self.name = name
		self.project = project
		self.githubName = githubName

class Developer(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	githubName = models.CharField(max_length =50, null = True, blank =True)
	pmAssigned = models.ForeignKey(PM, null = True, blank = True)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def __init__(self, name, githubName, pmAssigned, project):
		self.name = name
		self.pmAssigned = pmAssigned
		self.project = project
		self.githubName = githubName





class Milestone(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	progress = models.FloatField(default = 0)
	prevProgress = models.FloatField(default = 0)
	percentage = models.FloatField()
	dueDate = models.DateTimeField()

	def __init__(self, name, description, dueDate, percentage):
		self.name = name
		self.description = description
		self.dueDate = datetime.now()
		self.progress = 0
		# Section.objects.filter(milestone = self)

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

	# def __init__(slef, name, description, percentage, project, progress, developer, milestone):
	# 	self.name = name
	# 	self.description = description
	# 	self.percentage = percentage
	# 	self.progress = 0
	# 	self.project = project
	# 	self.developer = developer
	# 	self.milestone = milestone


	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = self.progress + progress
		progressUpdate = self.percentage * progress 
		self.project.update(progressUpdate)
		# self.milestone.update(progressUpdate)

	# def search_finished_section():
	# 	pass


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

	# def __init__(self, name, description, percentage, section):
	# 	self.name = name
	# 	self.description = description
	# 	self.percentage = percentage
	# 	self.progress = 0
	# 	self.section = section

	def __unicode__(self):
		return self.name









class Commit(models.Model):
	commitTime = models.DateTimeField()
	progress = models.FloatField()
	developer = models.ForeignKey(Developer)
	task = models.ForeignKey(Task)

	# def __init__(self, developer, task):
	# 	self.developer = developer
 #    	self.task = task
 #    	self.progress = progress
    	# self.task.update(progress)

	def __unicode__(self):
		return '{} {} {} {:.2f} {}'.format(self.developer.firstName, self.developer.lastName, 
			self.task.name, self.progress, self.commitTime)






















