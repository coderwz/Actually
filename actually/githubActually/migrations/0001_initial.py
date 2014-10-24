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
                ('description', models.CharField(max_length=1000)),
                ('progress', models.FloatField()),
                ('dueDate', models.DateTimeField()),
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
                ('description', models.CharField(max_length=1000)),
                ('startTime', models.DateTimeField(verbose_name=b'date the project starts')),
                ('finishTime', models.DateTimeField(verbose_name=b'date the project finishes')),
                ('progress', models.FloatField()),
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
                ('description', models.CharField(max_length=1000)),
                ('percentage', models.FloatField(verbose_name=b'the percentage in the the project')),
                ('progress', models.FloatField()),
                ('milestone', models.ForeignKey(to='githubActually.Milestone')),
                ('project', models.ForeignKey(to='githubActually.Project')),
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
                ('description', models.CharField(max_length=1000)),
                ('percentage', models.FloatField(verbose_name=b'the percentage in the the section')),
                ('progress', models.FloatField()),
                ('section', models.ForeignKey(to='githubActually.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('pmAssigned', models.ManyToManyField(related_name='pmAssigned_rel_+', to='githubActually.User')),
                ('project', models.ManyToManyField(to='githubActually.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='section',
            name='user',
            field=models.ForeignKey(to='githubActually.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='task',
            field=models.ForeignKey(to='githubActually.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commit',
            name='user',
            field=models.ForeignKey(to='githubActually.User'),
            preserve_default=True,
        ),
    ]
