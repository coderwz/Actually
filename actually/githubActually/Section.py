from django.db import models
import datetime
from django.utils import timezone
import Task

class Section(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the project')
	progress = models.FloatField()
	developer = models.ForeignKey(Developer, null = True, blank = True)
	project = models.ForeignKey(Project)
	milestone = models.ForeignKey(Milestone)

	def __unicode__(self):
	return self.name