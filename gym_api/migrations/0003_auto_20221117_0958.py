# Generated by Django 2.2 on 2022-11-17 08:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym_api', '0002_instructorfeeditem_memberfeeditem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MemberFeedItem',
            new_name='UserFeedItem',
        ),
        migrations.DeleteModel(
            name='InstructorFeedItem',
        ),
    ]