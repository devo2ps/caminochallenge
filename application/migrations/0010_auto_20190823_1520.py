# Generated by Django 2.2.4 on 2019-08-23 15:20

import application.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_remove_applicationobj_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationobj',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(db_index=True, default=application.models.default_dict),
        ),
    ]