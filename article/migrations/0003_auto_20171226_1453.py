# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20171225_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_time']},
        ),
        migrations.AddField(
            model_name='article',
            name='is_bio',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
