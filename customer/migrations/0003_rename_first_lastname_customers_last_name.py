# Generated by Django 4.2.1 on 2023-05-23 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customers_adress_alter_customers_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='first_lastname',
            new_name='last_name',
        ),
    ]
