# Generated by Django 3.2.4 on 2021-06-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_profile_handle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
