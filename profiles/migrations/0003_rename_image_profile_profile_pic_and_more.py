# Generated by Django 5.1.2 on 2024-11-10 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_pets_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pets_pic',
        ),
    ]
