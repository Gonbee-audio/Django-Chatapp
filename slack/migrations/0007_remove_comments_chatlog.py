# Generated by Django 2.2.13 on 2020-06-27 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0006_auto_20200627_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='chatlog',
        ),
    ]
