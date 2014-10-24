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

	def __unicode__(self):
		return self.name

class User(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	pmAssigned = models.ManyToManyField('self', null = True, blank = True)
	project = models.ManyToManyField(Project, null = True, blank = True)

	def __unicode__(self):
		return '{} {}'.format(self.firstName, self.lastName)

class Milestone(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	progress = models.FloatField()
	dueDate = models.DateTimeField()

	def __unicode__(self):
		return self.name



class Section(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the project')
	progress = models.FloatField()
	user = models.ForeignKey(User, null = True, blank = True)
	project = models.ForeignKey(Project)
	milestone = models.ForeignKey(Milestone)

	def __unicode__(self):
		return self.name


class Task(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the section')
	progress = models.FloatField()
	section = models.ForeignKey(Section)

	def __unicode__(self):
		return self.name





class Commit(models.Model):
	commitTime = models.DateTimeField()
	progress = models.FloatField()
	user = models.ForeignKey(User)
	task = models.ForeignKey(Task)

	def __unicode__(self):
		return '{} {} {} {:.2f} {}'.format(self.user.firstName, self.user.lastName, self.task.name, self.progress, self.commitTime)























