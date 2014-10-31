# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubActually', '0004_auto_20141029_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(to='githubActually.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='milestone',
            name='percentage',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='milestone',
            name='prevProgress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='prevProgress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='repo',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='repoOwner',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='prevProgress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='prevProgress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='milestone',
            name='progress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pm',
            name='githubName',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='progress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='progress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='project',
            field=models.ForeignKey(to='githubActually.Project', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='progress',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
