# Generated by Django 4.2.3 on 2023-07-19 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiorecord',
            old_name='audio_file',
            new_name='audio',
        ),
    ]
