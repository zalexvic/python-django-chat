# Generated by Django 3.2.4 on 2021-06-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='message',
            name='room_id',
            field=models.IntegerField(null=True),
        ),
    ]