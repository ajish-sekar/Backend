# Generated by Django 2.2.5 on 2019-09-30 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_registeredsellers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisteredSellers',
            new_name='RegisteredSeller',
        ),
    ]