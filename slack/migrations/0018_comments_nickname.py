# Generated by Django 2.2.13 on 2020-07-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0017_chatmessage_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='nickname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
