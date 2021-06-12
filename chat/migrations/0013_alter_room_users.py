# Generated by Django 3.2.4 on 2021-06-12 19:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0012_alter_room_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='users',
            field=models.ManyToManyField(related_name='guest_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
