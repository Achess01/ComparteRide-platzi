# Generated by Django 3.2.14 on 2022-07-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0003_auto_20220729_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='remaining_invitation',
            new_name='remaining_invitations',
        ),
    ]
