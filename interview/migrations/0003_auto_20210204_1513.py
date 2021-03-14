# Generated by Django 3.1.4 on 2021-02-04 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0002_comment_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='likes',
        ),
        migrations.AddField(
            model_name='interview',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='공감수'),
        ),
    ]
