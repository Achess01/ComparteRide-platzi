# Generated by Django 3.2.14 on 2022-07-25 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circle',
            old_name='members_list',
            new_name='members_limit',
        ),
    ]
