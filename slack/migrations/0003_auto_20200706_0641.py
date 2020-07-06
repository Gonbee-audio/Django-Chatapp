# Generated by Django 2.2.14 on 2020-07-05 21:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0002_secredmessage_yourname'),
    ]

    operations = [
        migrations.AddField(
            model_name='secredmessage',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='secredmessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='secredmessage',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]