# Generated by Django 4.1.4 on 2022-12-20 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Category',
        ),
    ]
