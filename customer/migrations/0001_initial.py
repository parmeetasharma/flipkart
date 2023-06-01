# Generated by Django 4.2.1 on 2023-05-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('first_lastname', models.CharField(blank=True, max_length=15, null=True)),
                ('mobile_no', models.IntegerField(blank=True, max_length=15, null=True)),
                ('adress', models.TextField(blank=True, max_length=15, null=True)),
                ('age', models.IntegerField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
