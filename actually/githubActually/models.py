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
	progress = models.FloatField()

	def __init__(self, name, description, startTime):
		self.name = name
		self.description = description
		self.startTime = startTime
		self.progress = 0

	def __unicode__(self):
		return self.name

	def update(self, progress):
		pass


class User(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	pmAssigned = models.ManyToManyField('self', null = True, blank = True)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def __unicode__(self):
		return '{} {}'.format(self.firstName, self.lastName)

	def __init__(self, name, pmAssigned, project):
		self.name = name
		self.pmAssigned = pmAssigned
		self.project = project

class Milestone(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	progress = models.FloatField()
	dueDate = models.DateTimeField()

	def __init__(self, name, description, dueDate):
		self.name = name
		self.description = description
		self.dueDate = datetime.now()
		self.progress = 0

	def __unicode__(self):
		return self.name

	def update(self, progress):
		pass



class Section(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the project')
	progress = models.FloatField()
	user = models.ForeignKey(User, null = True, blank = True)
	project = models.ForeignKey(Project)
	milestone = models.ForeignKey(Milestone)

	def __init__(slef, name, description, percentage, project, progress, user, milestone):
		self.name = name
		self.description = description
		self.percentage = percentage
		self.progress = 0
		self.project = project
		self.user = user
		self.milestone = milestone


	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.progress = self.percentage * progress
		self.project(progress)
		self.milestone(progress)

	def search_finished_section():
		pass


class Task(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the section')
	progress = models.FloatField()
	section = models.ForeignKey(Section)

	def __init__(self, name, description, percentage, section):
		self.name = name
		self.description = description
		self.percentage = percentage
		self.progress = 0
		self.section = section

	def __unicode__(self):
		return self.name

	def update(self, progress):
		self.progress = self.percentage * progress
		self.section.update(self.progress)

	def search_finished_task(self):
		pass






class Commit(models.Model):
	commitTime = models.DateTimeField()
	progress = models.FloatField()
	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)

	def __unicode__(self):
		return '{} {} {} {:.2f} {}'.format(self.user.firstName, self.user.lastName, self.task.name, self.progress, self.commitTime)

    def __init__(self, user, task, progress):
    	self.user = user
    	self.task = task
    	self.progress = progress
    	self.task.update(progress)






















