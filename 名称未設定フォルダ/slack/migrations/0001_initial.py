# Generated by Django 2.2.13 on 2020-06-26 19:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images')),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('favorite', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=1000)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images')),
                ('chatlog', models.IntegerField(default=0, null=True)),
                ('chatmessage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='slack.ChatMessage')),
            ],
        ),
    ]
