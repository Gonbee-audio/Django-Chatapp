# Generated by Django 2.2.13 on 2020-06-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0010_auto_20200627_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icon'),
        ),
    ]