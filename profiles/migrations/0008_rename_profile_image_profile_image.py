# Generated by Django 5.1.2 on 2024-11-23 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_rename_profile_pic_profile_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_image',
            new_name='image',
        ),
    ]
