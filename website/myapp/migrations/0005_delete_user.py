# Generated by Django 5.0.1 on 2024-05-17 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_customeuser_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
