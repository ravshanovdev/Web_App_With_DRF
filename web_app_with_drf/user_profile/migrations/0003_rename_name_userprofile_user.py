# Generated by Django 5.0 on 2024-01-07 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='user',
        ),
    ]
