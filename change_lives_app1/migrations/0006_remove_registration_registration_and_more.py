# Generated by Django 4.1.5 on 2023-03-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_lives_app1', '0005_alter_registration_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='registration',
        ),
        migrations.AddField(
            model_name='registration',
            name='registration_no',
            field=models.IntegerField(default=789),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]