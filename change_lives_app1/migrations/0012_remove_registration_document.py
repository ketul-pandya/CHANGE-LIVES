# Generated by Django 4.1.5 on 2023-03-30 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_lives_app1', '0011_alter_registration_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='document',
        ),
    ]