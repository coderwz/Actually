# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('githubActually', '0002_auto_20141023_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='githubName',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
