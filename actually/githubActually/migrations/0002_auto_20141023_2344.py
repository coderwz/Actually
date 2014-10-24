# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubActually', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='finishTime',
            field=models.DateTimeField(null=True, verbose_name=b'date the project finishes', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(blank=True, to='githubActually.User', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pmAssigned',
            field=models.ManyToManyField(related_name='pmAssigned_rel_+', null=True, to=b'githubActually.User', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='project',
            field=models.ManyToManyField(to=b'githubActually.Project', null=True, blank=True),
        ),
    ]
