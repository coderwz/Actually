# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commitTime', models.DateTimeField()),
                ('progress', models.FloatField()),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('githubName', models.CharField(max_length=50)),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('progress', models.FloatField(default=0)),
                ('prevProgress', models.FloatField(default=0)),
                ('percentage', models.FloatField(null=True)),
                ('dueDate', models.DateField()),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
                ('developer', models.ManyToManyField(to='githubActually.Developer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('githubName', models.CharField(default=0, max_length=50)),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('startTime', models.DateField(verbose_name=b'date the project starts')),
                ('finishTime', models.DateField(null=True, verbose_name=b'date the project finishes', blank=True)),
                ('progress', models.FloatField(default=0)),
                ('prevProgress', models.FloatField(default=0)),
                ('repo', models.CharField(max_length=100, null=True)),
                ('repoOwner', models.CharField(max_length=100, null=True, blank=True)),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('percentage', models.FloatField(verbose_name=b'the percentage in the the project')),
                ('progress', models.FloatField(default=0)),
                ('prevProgress', models.FloatField(default=0)),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
                ('developer', models.OneToOneField(null=True, blank=True, to='githubActually.Developer')),
                ('project', models.ForeignKey(to='githubActually.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('percentage', models.FloatField(verbose_name=b'the percentage in the the section')),
                ('progress', models.FloatField(default=0)),
                ('prevProgress', models.FloatField(default=0)),
                ('optional1', models.CharField(max_length=100, null=True, blank=True)),
                ('optional2', models.CharField(max_length=100, null=True, blank=True)),
                ('optional3', models.CharField(max_length=100, null=True, blank=True)),
                ('developer', models.ForeignKey(blank=True, to='githubActually.Developer', null=True)),
                ('milestone', models.ForeignKey(to='githubActually.Milestone')),
                ('section', models.ForeignKey(to='githubActually.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pm',
            name='project',
            field=models.ManyToManyField(to='githubActually.Project', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(to='githubActually.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developer',
            name='pmAssigned',
            field=models.ForeignKey(blank=True, to='githubActually.PM', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='developer',
            name='project',
            field=models.ManyToManyField(to='githubActually.Project', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='developer',
            field=models.ForeignKey(to='githubActually.Developer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(to='githubActually.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='task',
            field=models.ForeignKey(to='githubActually.Task'),
            preserve_default=True,
        ),
    ]
