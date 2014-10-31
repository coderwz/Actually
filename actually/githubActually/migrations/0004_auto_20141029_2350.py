# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubActually', '0003_user_githubname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('githubName', models.CharField(max_length=50, null=True, blank=True)),
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
                ('githubName', models.CharField(max_length=50, null=True, blank=True)),
                ('project', models.ManyToManyField(to='githubActually.Project', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='pmAssigned',
        ),
        migrations.RemoveField(
            model_name='user',
            name='project',
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
        migrations.RemoveField(
            model_name='commit',
            name='user',
        ),
        migrations.RemoveField(
            model_name='section',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='commit',
            name='developer',
            field=models.ForeignKey(default=1, to='githubActually.Developer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='developer',
            field=models.ForeignKey(blank=True, to='githubActually.Developer', null=True),
            preserve_default=True,
        ),
    ]
