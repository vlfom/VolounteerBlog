# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogengine', '0009_auto_20150328_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subscribers',
            field=models.ManyToManyField(related_name='post_requests_created', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(related_name='author_of_post', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
