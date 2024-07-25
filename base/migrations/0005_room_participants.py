# Generated by Django 5.0.7 on 2024-07-19 03:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_msgs_delete_msg'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]