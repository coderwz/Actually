from django.db import models
import datetime
from django.utils import timezone

class Task(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 1000, null = True, blank = True)
	percentage = models.FloatField('the percentage in the the section')
	progress = models.FloatField(default = 0)
	prevProgress = models.FloatField(default = 0)
	section = models.ForeignKey(Section)
	def update(self, progress):
		self.prevProgress = self.progress
		self.progress = self.percentage * progress
		self.section.update(self.progress)