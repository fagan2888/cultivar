# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0003_auto_20160722_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('version', models.PositiveIntegerField()),
                ('bundle_available', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'dataset_versions',
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
        migrations.RemoveField(
            model_name='datafile',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='version',
        ),
        migrations.AddField(
            model_name='datasetversion',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='dataset.Dataset'),
        ),
        migrations.AddField(
            model_name='datafile',
            name='version',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='dataset.DatasetVersion'),
            preserve_default=False,
        ),
    ]
