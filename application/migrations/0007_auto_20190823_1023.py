# Generated by Django 2.2.4 on 2019-08-23 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_statusobj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusobj',
            old_name='what',
            new_name='stat',
        ),
    ]
