# Generated by Django 4.1.5 on 2023-05-09 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_company_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='created_by',
        ),
    ]
