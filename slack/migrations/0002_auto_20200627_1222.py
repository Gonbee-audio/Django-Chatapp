# Generated by Django 2.2.13 on 2020-06-27 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='chatmessage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slack.ChatMessage'),
        ),
    ]