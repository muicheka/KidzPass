# Generated by Django 2.1.2 on 2018-11-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_remove_profile_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='admin',
            field=models.BooleanField(default=False, null=True),
        ),
    ]