# Generated by Django 3.2.4 on 2021-06-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20210612_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]