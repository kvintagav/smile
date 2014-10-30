# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True, parent_link=True)),
                ('about', models.TextField(verbose_name='about')),
                ('date_pay', models.DateTimeField(verbose_name='date_pay')),
                ('about_short', models.TextField(verbose_name='about_short')),
            ],
            options={
                'db_table': 'Photographer',
            },
            bases=('auth.user',),
        ),
    ]
