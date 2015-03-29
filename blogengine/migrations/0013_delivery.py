# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogengine', '0012_post_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('delivery_date', models.DateTimeField()),
                ('slug', models.SlugField(max_length=40, unique=True, null=True, blank=True)),
                ('author', models.ForeignKey(related_name='delivery_author', to=settings.AUTH_USER_MODEL)),
                ('recipients', models.ManyToManyField(related_name='delivery_recipients', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ['-delivery_date'],
            },
            bases=(models.Model,),
        ),
    ]
