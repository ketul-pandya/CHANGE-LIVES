# Generated by Django 4.1.5 on 2023-03-30 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_lives_app1', '0010_alter_registration_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
