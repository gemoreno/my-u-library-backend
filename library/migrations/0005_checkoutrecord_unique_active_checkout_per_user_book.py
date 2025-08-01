# Generated by Django 5.2.4 on 2025-08-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_is_returned_checkoutrecord_returned'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='checkoutrecord',
            constraint=models.UniqueConstraint(condition=models.Q(('returned', False)), fields=('user', 'book'), name='unique_active_checkout_per_user_book'),
        ),
    ]
