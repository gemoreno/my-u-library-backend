# Generated by Django 5.2.4 on 2025-08-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutrecord',
            old_name='student',
            new_name='user',
        ),
    ]
