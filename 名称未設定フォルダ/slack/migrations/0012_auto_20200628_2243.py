# Generated by Django 2.2.13 on 2020-06-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0011_auto_20200628_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='icon',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='comments',
            name='icon',
            field=models.CharField(max_length=1000),
        ),
    ]
