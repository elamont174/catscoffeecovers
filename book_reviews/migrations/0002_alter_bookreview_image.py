# Generated by Django 5.1.2 on 2024-11-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='image',
            field=models.ImageField(blank=True, default='../default_kejxo8', upload_to='images/'),
        ),
    ]