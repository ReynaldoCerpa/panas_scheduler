# Generated by Django 5.0.6 on 2024-06-06 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='creation_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='banner',
        ),
    ]